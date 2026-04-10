"""
U8 Archive (.arc) reader/writer for Nintendo Wii.

The U8 format is a simple archive used by Nintendo Wii games (including NSMBW).
Structure:
  - 32-byte header: magic (0x55AA382D), root node offset, data offset, file sizes
  - Node table: each node is 12 bytes (type/nameoff, data_offset, size_or_next)
  - String table: null-terminated filenames
  - File data: concatenated file contents (aligned to 32 bytes)

All multi-byte values are Big Endian.
"""

import struct
import os


class U8Archive:
    """Read and write U8 .arc archives with byte-level fidelity."""

    MAGIC = 0x55AA382D
    HEADER_SIZE = 32
    NODE_SIZE = 12

    def __init__(self):
        self.files = []  # list of (path, data) tuples

    @classmethod
    def load(cls, data: bytes) -> 'U8Archive':
        """Parse a U8 archive from raw bytes."""
        arc = cls()

        # --- Header ---
        if len(data) < cls.HEADER_SIZE:
            raise ValueError("Data too short for U8 header")

        magic, rootnode_offset, header_size, data_offset = struct.unpack_from(
            '>IIII', data, 0
        )
        if magic != cls.MAGIC:
            raise ValueError(f"Bad U8 magic: 0x{magic:08X} (expected 0x{cls.MAGIC:08X})")

        # --- Root node ---
        root_type_name = struct.unpack_from('>I', data, rootnode_offset)[0]
        root_type = (root_type_name >> 24) & 0xFF
        if root_type != 1:
            raise ValueError(f"Root node is not a directory (type={root_type})")

        root_size = struct.unpack_from('>I', data, rootnode_offset + 8)[0]
        node_count = root_size  # root's "size" field = total node count

        # --- String table ---
        string_table_offset = rootnode_offset + node_count * cls.NODE_SIZE

        def read_string(offset):
            end = data.index(b'\x00', string_table_offset + offset)
            return data[string_table_offset + offset:end].decode('ascii')

        # --- Parse all nodes ---
        nodes = []
        for i in range(node_count):
            off = rootnode_offset + i * cls.NODE_SIZE
            type_name_off = struct.unpack_from('>I', data, off)[0]
            data_off = struct.unpack_from('>I', data, off + 4)[0]
            size_or_next = struct.unpack_from('>I', data, off + 8)[0]

            ntype = (type_name_off >> 24) & 0xFF
            name_off = type_name_off & 0x00FFFFFF

            name = read_string(name_off) if i > 0 else ''
            nodes.append({
                'type': ntype,  # 0=file, 1=dir
                'name': name,
                'data_offset': data_off,
                'size': size_or_next,
            })

        # --- Build file list with paths ---
        dir_stack = []  # stack of (dir_name, end_index)

        for i, node in enumerate(nodes):
            if i == 0:
                # Root directory
                dir_stack.append(('', node['size']))
                continue

            # Pop directories that have ended
            while dir_stack and i >= dir_stack[-1][1]:
                dir_stack.pop()

            # Build current path
            path_parts = [d[0] for d in dir_stack if d[0]] + [node['name']]
            full_path = '/'.join(path_parts)

            if node['type'] == 1:
                # Directory
                dir_stack.append((node['name'], node['size']))
            else:
                # File
                file_data = data[node['data_offset']:node['data_offset'] + node['size']]
                arc.files.append((full_path, file_data))

        return arc

    def pack(self) -> bytes:
        """Serialize this archive back to U8 binary format."""
        # Rebuild directory structure from file paths
        all_entries = self._build_entry_tree()

        # Calculate sizes
        node_count = len(all_entries)
        string_table = self._build_string_table(all_entries)
        nodes_and_strings_size = node_count * self.NODE_SIZE + len(string_table)

        # Align to 32 bytes
        rootnode_offset = self.HEADER_SIZE
        header_and_nodes_size = rootnode_offset + nodes_and_strings_size
        data_start = _align(header_and_nodes_size, 32)

        # Calculate file data offsets
        current_data_offset = data_start
        file_offsets = {}
        file_entries = [e for e in all_entries if e['type'] == 0]
        for idx, entry in enumerate(file_entries):
            file_offsets[entry['path']] = current_data_offset
            current_data_offset += entry['size']
            # Only align between files, NOT after the last one
            if idx < len(file_entries) - 1:
                current_data_offset = _align(current_data_offset, 32)

        total_size = current_data_offset

        # --- Write header ---
        result = bytearray(total_size)
        struct.pack_into('>IIII', result, 0,
                         self.MAGIC,
                         rootnode_offset,
                         nodes_and_strings_size,
                         data_start)
        # Pad rest of header to 32 bytes (bytes 16-31 are zero)

        # --- Write nodes ---
        string_offsets = self._calc_string_offsets(all_entries, string_table)

        for i, entry in enumerate(all_entries):
            off = rootnode_offset + i * self.NODE_SIZE
            type_name = (entry['type'] << 24) | string_offsets[i]

            if entry['type'] == 1:
                # Directory: data_offset = parent index, size = next sibling index
                struct.pack_into('>III', result, off,
                                 type_name,
                                 entry.get('parent_idx', 0),
                                 entry['next_idx'])
            else:
                # File
                foff = file_offsets[entry['path']]
                struct.pack_into('>III', result, off,
                                 type_name, foff, entry['size'])

        # --- Write string table ---
        st_offset = rootnode_offset + node_count * self.NODE_SIZE
        result[st_offset:st_offset + len(string_table)] = string_table

        # --- Write file data ---
        for entry in all_entries:
            if entry['type'] == 0:
                foff = file_offsets[entry['path']]
                fdata = entry['data']
                result[foff:foff + len(fdata)] = fdata

        return bytes(result)

    def get_file(self, path: str) -> bytes:
        """Get file data by path."""
        for fpath, fdata in self.files:
            if fpath == path:
                return fdata
        raise KeyError(f"File not found in archive: {path}")

    def set_file(self, path: str, data: bytes):
        """Set/replace file data by path."""
        for i, (fpath, _) in enumerate(self.files):
            if fpath == path:
                self.files[i] = (path, data)
                return
        self.files.append((path, data))

    def list_files(self) -> list:
        """Return list of file paths in the archive."""
        return [path for path, _ in self.files]

    def _build_entry_tree(self):
        """Build a flat list of entries in DFS order (dir, then children)."""
        # Build a tree of directories and files
        dir_children = {}   # dir_path -> list of child dir paths
        dir_files = {}      # dir_path -> list of (file_path, data)
        all_dirs = set()

        for path, data in self.files:
            parts = path.split('/')
            for i in range(1, len(parts)):
                d = '/'.join(parts[:i])
                all_dirs.add(d)
            parent = '/'.join(parts[:-1])
            dir_files.setdefault(parent, []).append((path, data))

        # Build directory children map
        for d in sorted(all_dirs):
            parent = '/'.join(d.split('/')[:-1])
            dir_children.setdefault(parent, []).append(d)

        # DFS traversal to produce flat entry list
        entries = []

        def add_dir(dpath, parent_idx):
            idx = len(entries)
            name = dpath.split('/')[-1] if dpath else ''
            entries.append({
                'type': 1,
                'name': name,
                'path': dpath,
                'parent_idx': parent_idx,
                'next_idx': 0,  # Set later
            })
            # Add child directories (sorted)
            for child_dir in sorted(dir_children.get(dpath, [])):
                add_dir(child_dir, idx)
            # Add files in this directory (sorted)
            for fpath, fdata in sorted(dir_files.get(dpath, []),
                                        key=lambda x: x[0]):
                entries.append({
                    'type': 0,
                    'name': fpath.split('/')[-1],
                    'path': fpath,
                    'parent_idx': idx,
                    'data': fdata,
                    'size': len(fdata),
                })

        add_dir('', 0)

        # Calculate next_idx for directories
        total = len(entries)
        entries[0]['next_idx'] = total

        for i, entry in enumerate(entries):
            if entry['type'] == 1 and i > 0:
                my_path = entry['path'] + '/'
                next_idx = total
                for j in range(i + 1, total):
                    jpath = entries[j].get('path', '')
                    if not jpath.startswith(my_path) and jpath != entry['path']:
                        next_idx = j
                        break
                entries[i]['next_idx'] = next_idx

        return entries

    def _build_string_table(self, entries):
        """Build the string table (concatenated null-terminated names)."""
        parts = []
        for entry in entries:
            parts.append(entry['name'].encode('ascii') + b'\x00')
        return b''.join(parts)

    def _calc_string_offsets(self, entries, string_table):
        """Calculate the offset of each entry's name in the string table."""
        offsets = []
        pos = 0
        for entry in entries:
            offsets.append(pos)
            pos += len(entry['name'].encode('ascii')) + 1
        return offsets


def _align(value, alignment):
    """Align value up to the next multiple of alignment."""
    remainder = value % alignment
    if remainder == 0:
        return value
    return value + (alignment - remainder)
