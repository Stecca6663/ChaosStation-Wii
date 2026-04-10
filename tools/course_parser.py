"""
Course binary parser and serializer for NSMBW.

Handles all 14 blocks of course.bin and the layer bgdat files.
All values are Big Endian (Wii PowerPC architecture).
"""

import struct
from dataclasses import dataclass, field
from typing import List, Optional


# ──────────────────────────────────────────────
# Data structures for each block
# ──────────────────────────────────────────────

@dataclass
class Tileset:
    """Block 1: 4 tileset names, 32 bytes each."""
    slot0: str = "Pa0_jyotyu"
    slot1: str = ""
    slot2: str = ""
    slot3: str = ""


@dataclass
class AreaSettings:
    """Block 2: Area-wide settings (20 bytes)."""
    eventbits_lo: int = 0
    eventbits_hi: int = 0
    wrap: int = 0
    time_limit: int = 300
    credits: bool = False
    unk1: int = 100
    unk2: int = 100
    unk3: int = 100
    start_entrance: int = 0
    ambush: bool = False
    toad_house_type: int = 0


@dataclass
class Bounding:
    """Block 3: Zone camera bounding (24 bytes each)."""
    upper: int = 0
    lower: int = 0
    upper2: int = 0
    lower2: int = 0
    bound_id: int = 0
    mp_cam_zoom: int = 15
    upper3: int = 0
    lower3: int = 0


@dataclass
class UnknownBlock4:
    """Block 4: Unknown options (8 bytes)."""
    raw: bytes = b'\x00\x00\x00\x02\x00\x42\x00\x00'


@dataclass
class Background:
    """Block 5/6: Background settings (24 bytes each)."""
    bg_id: int = 0
    x_scroll: int = 0
    y_scroll: int = 0
    y_pos: int = 0
    x_pos: int = 0
    bg1: int = 10
    bg2: int = 258
    bg3: int = 10
    zoom: int = 0
    unk: int = 0


@dataclass
class Entrance:
    """Block 7: Entrance definition (20 bytes)."""
    x: int = 0
    y: int = 0
    unk1: int = 0
    unk2: int = 0
    entrance_id: int = 0
    dest_area: int = 0
    dest_entrance: int = 0
    etype: int = 0  # 0=normal, 1=pipe, 2=door, 3=vine
    unk3: int = 0
    zone_id: int = 0
    layer: int = 0
    path: int = 0
    settings: int = 0
    leave_level: int = 0
    cp_direction: int = 0


@dataclass
class Sprite:
    """Block 8: Sprite/actor (16 bytes, terminated by FFFFFFFF)."""
    stype: int = 0
    x: int = 0
    y: int = 0
    spritedata: bytes = b'\x00' * 6
    zone_id: int = 0
    extra_byte: int = 0


@dataclass
class Zone:
    """Block 10: Zone definition (24 bytes)."""
    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 384
    model_dark: int = 0
    terrain_dark: int = 0
    zone_id: int = 0
    bound_id: int = 0
    cam_mode: int = 0
    cam_zoom: int = 0
    visibility: int = 0
    bg_a: int = 0
    bg_b: int = 0
    cam_track: int = 0
    music: int = 1
    sfx: int = 0


@dataclass
class Location:
    """Block 11: Location rectangle (12 bytes)."""
    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 0
    loc_id: int = 0


@dataclass
class Path:
    """Block 13: Path definition (8 bytes)."""
    path_id: int = 0
    unk1: int = 0
    start_node: int = 0
    node_count: int = 0
    unk2: int = 0


@dataclass
class PathNode:
    """Block 14: Path node (16 bytes)."""
    x: int = 0
    y: int = 0
    speed: float = 1.0
    accel: float = 1.0
    delay: int = 0


@dataclass
class LayerObject:
    """Layer terrain object (10 bytes, terminated by 0xFFFF)."""
    tileset: int = 0      # 0-3 (which tileset)
    obj_type: int = 0     # object type within the tileset
    x: int = 0            # tile X position
    y: int = 0            # tile Y position
    w: int = 1            # width in tiles
    h: int = 1            # height in tiles


@dataclass
class CourseArea:
    """All parsed data for one course area."""
    tileset: Tileset = field(default_factory=Tileset)
    settings: AreaSettings = field(default_factory=AreaSettings)
    boundings: List[Bounding] = field(default_factory=list)
    block4: UnknownBlock4 = field(default_factory=UnknownBlock4)
    bg_a: List[Background] = field(default_factory=list)
    bg_b: List[Background] = field(default_factory=list)
    entrances: List[Entrance] = field(default_factory=list)
    sprites: List[Sprite] = field(default_factory=list)
    loaded_sprites: List[int] = field(default_factory=list)
    zones: List[Zone] = field(default_factory=list)
    locations: List[Location] = field(default_factory=list)
    cam_profiles: bytes = b''  # Block 12 raw
    paths: List[Path] = field(default_factory=list)
    path_nodes: List[PathNode] = field(default_factory=list)
    layer0: List[LayerObject] = field(default_factory=list)
    layer1: List[LayerObject] = field(default_factory=list)
    layer2: List[LayerObject] = field(default_factory=list)


# ──────────────────────────────────────────────
# Parser
# ──────────────────────────────────────────────

def parse_course_bin(data: bytes) -> CourseArea:
    """Parse a course.bin binary into a CourseArea dataclass."""
    area = CourseArea()

    # Parse header: 14 blocks × (offset, size)
    blocks = []
    for i in range(14):
        off, sz = struct.unpack_from('>II', data, i * 8)
        blocks.append((off, sz))

    # Block 1: Tilesets (128 bytes = 4 × 32-byte strings)
    off, sz = blocks[0]
    if sz >= 128:
        area.tileset = Tileset(
            slot0=_read_str32(data, off),
            slot1=_read_str32(data, off + 32),
            slot2=_read_str32(data, off + 64),
            slot3=_read_str32(data, off + 96),
        )

    # Block 2: Area settings (20 bytes)
    off, sz = blocks[1]
    if sz >= 20:
        ev_lo, ev_hi, wrap, time, cred, u1, u2, u3, start_ent, amb, th = \
            struct.unpack_from('>IIHh?BBBBx?B', data, off)
        area.settings = AreaSettings(
            eventbits_lo=ev_lo, eventbits_hi=ev_hi,
            wrap=wrap, time_limit=time, credits=cred,
            unk1=u1, unk2=u2, unk3=u3,
            start_entrance=start_ent, ambush=amb,
            toad_house_type=th
        )

    # Block 3: Bounding (24 bytes each)
    off, sz = blocks[2]
    count = sz // 24
    for i in range(count):
        p = off + i * 24
        ub, lb, ub2, lb2, bid, mpz, ub3, lb3 = \
            struct.unpack_from('>iiiiHHhh', data, p)
        area.boundings.append(Bounding(
            upper=ub, lower=lb, upper2=ub2, lower2=lb2,
            bound_id=bid, mp_cam_zoom=mpz, upper3=ub3, lower3=lb3
        ))

    # Block 4: Unknown (8 bytes raw)
    off, sz = blocks[3]
    if sz > 0:
        area.block4 = UnknownBlock4(raw=data[off:off + sz])

    # Block 5: BG-A (24 bytes each)
    off, sz = blocks[4]
    area.bg_a = _parse_backgrounds(data, off, sz)

    # Block 6: BG-B (24 bytes each)
    off, sz = blocks[5]
    area.bg_b = _parse_backgrounds(data, off, sz)

    # Block 7: Entrances (20 bytes each)
    off, sz = blocks[6]
    count = sz // 20
    for i in range(count):
        p = off + i * 20
        x, y, unk1, unk2, eid, darea, dent, etype, zid, layer, path, settings, leave, cpdir = \
            struct.unpack_from('>HHHHBBBBxBBBHBB', data, p)
        area.entrances.append(Entrance(
            x=x, y=y, unk1=unk1, unk2=unk2,
            entrance_id=eid, dest_area=darea, dest_entrance=dent,
            etype=etype, zone_id=zid, layer=layer,
            path=path, settings=settings, leave_level=leave,
            cp_direction=cpdir
        ))

    # Block 8: Sprites (16 bytes each + FFFFFFFF terminator)
    # Format: >HHH6sBBxx = type(2) x(2) y(2) spritedata(6) zone(1) extra(1) pad(2) = 16 bytes
    off, sz = blocks[7]
    pos = off
    end = off + sz
    while pos + 16 <= end:
        check = struct.unpack_from('>I', data, pos)[0]
        if check == 0xFFFFFFFF:
            break
        stype, sx, sy = struct.unpack_from('>HHH', data, pos)
        sdata = data[pos + 6:pos + 12]
        szid = data[pos + 12]
        extra = data[pos + 13]
        area.sprites.append(Sprite(
            stype=stype, x=sx, y=sy,
            spritedata=sdata, zone_id=szid, extra_byte=extra
        ))
        pos += 16

    # Block 9: Loaded sprite types (4 bytes each: u16 type + 2 pad)
    off, sz = blocks[8]
    count = sz // 4
    for i in range(count):
        st = struct.unpack_from('>H', data, off + i * 4)[0]
        area.loaded_sprites.append(st)

    # Block 10: Zones (24 bytes each)
    off, sz = blocks[9]
    count = sz // 24
    for i in range(count):
        p = off + i * 24
        x, y, w, h, md, td, zid, bid, cmode, czoom, vis, bga, bgb, ctrack, mus, sfx = \
            struct.unpack_from('>HHHHHHBBBBxBBBBxBB', data, p)
        area.zones.append(Zone(
            x=x, y=y, w=w, h=h,
            model_dark=md, terrain_dark=td,
            zone_id=zid, bound_id=bid,
            cam_mode=cmode, cam_zoom=czoom,
            visibility=vis, bg_a=bga, bg_b=bgb,
            cam_track=ctrack, music=mus, sfx=sfx
        ))

    # Block 11: Locations (12 bytes each)
    off, sz = blocks[10]
    count = sz // 12
    for i in range(count):
        p = off + i * 12
        x, y, w, h, lid = struct.unpack_from('>HHHHBxxx', data, p)
        area.locations.append(Location(x=x, y=y, w=w, h=h, loc_id=lid))

    # Block 12: Camera profiles (raw)
    off, sz = blocks[11]
    area.cam_profiles = data[off:off + sz]

    # Block 13: Paths (8 bytes each)
    off, sz = blocks[12]
    count = sz // 8
    for i in range(count):
        p = off + i * 8
        pid, u1, sn, nc, u2 = struct.unpack_from('>BBHHH', data, p)
        area.paths.append(Path(path_id=pid, unk1=u1, start_node=sn, node_count=nc, unk2=u2))

    # Block 14: Path nodes (16 bytes each)
    off, sz = blocks[13]
    count = sz // 16
    for i in range(count):
        p = off + i * 16
        nx, ny, spd, acc, delay = struct.unpack_from('>HHffhxx', data, p)
        area.path_nodes.append(PathNode(x=nx, y=ny, speed=spd, accel=acc, delay=delay))

    return area


def serialize_course_bin(area: CourseArea) -> bytes:
    """Serialize a CourseArea back to binary course.bin format."""
    # Build each block
    b1 = _ser_tilesets(area.tileset)
    b2 = _ser_settings(area.settings)
    b3 = _ser_boundings(area.boundings)
    b4 = area.block4.raw
    b5 = _ser_backgrounds(area.bg_a)
    b6 = _ser_backgrounds(area.bg_b)
    b7 = _ser_entrances(area.entrances)
    b8 = _ser_sprites(area.sprites)
    b9 = _ser_loaded_sprites(area.loaded_sprites)
    b10 = _ser_zones(area.zones)
    b11 = _ser_locations(area.locations)
    b12 = area.cam_profiles
    b13 = _ser_paths(area.paths)
    b14 = _ser_path_nodes(area.path_nodes)

    all_blocks = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14]

    # Calculate header (14 entries × 8 bytes = 112 bytes)
    header_size = 14 * 8
    current_offset = header_size

    offsets_sizes = []
    for block_data in all_blocks:
        offsets_sizes.append((current_offset, len(block_data)))
        current_offset += len(block_data)

    # Build header
    header = bytearray()
    for off, sz in offsets_sizes:
        header += struct.pack('>II', off, sz)

    # Concatenate
    result = bytes(header)
    for block_data in all_blocks:
        result += block_data

    return result


def parse_layer_data(data: bytes) -> List[LayerObject]:
    """Parse a bgdatLx.bin layer file into LayerObjects."""
    objects = []
    pos = 0
    while pos + 10 <= len(data):
        combined = struct.unpack_from('>H', data, pos)[0]
        if combined == 0xFFFF:
            break
        tileset = (combined >> 12) & 0xF
        obj_type = combined & 0x0FFF
        x, y, w, h = struct.unpack_from('>HHHH', data, pos + 2)
        objects.append(LayerObject(
            tileset=tileset, obj_type=obj_type,
            x=x, y=y, w=w, h=h
        ))
        pos += 10
    return objects


def serialize_layer_data(objects: List[LayerObject]) -> bytes:
    """Serialize LayerObjects back to bgdatLx.bin format."""
    result = bytearray()
    for obj in objects:
        combined = ((obj.tileset & 0xF) << 12) | (obj.obj_type & 0x0FFF)
        result += struct.pack('>HHHHH', combined, obj.x, obj.y, obj.w, obj.h)
    result += struct.pack('>H', 0xFFFF)  # Terminator
    return bytes(result)


# ──────────────────────────────────────────────
# Internal serializers
# ──────────────────────────────────────────────

def _read_str32(data, offset):
    """Read a 32-byte null-terminated string."""
    raw = data[offset:offset + 32]
    try:
        return raw.split(b'\x00')[0].decode('ascii')
    except:
        return ''


def _ser_tilesets(ts: Tileset) -> bytes:
    """Serialize Block 1: 128 bytes."""
    def pad32(s):
        b = s.encode('ascii') if s else b''
        return b.ljust(32, b'\x00')
    return pad32(ts.slot0) + pad32(ts.slot1) + pad32(ts.slot2) + pad32(ts.slot3)


def _ser_settings(s: AreaSettings) -> bytes:
    """Serialize Block 2: 20 bytes."""
    return struct.pack('>IIHh?BBBBx?B',
                       s.eventbits_lo, s.eventbits_hi,
                       s.wrap, s.time_limit, s.credits,
                       s.unk1, s.unk2, s.unk3,
                       s.start_entrance, s.ambush,
                       s.toad_house_type)


def _ser_boundings(bounds: List[Bounding]) -> bytes:
    """Serialize Block 3: 24 bytes each."""
    result = bytearray()
    for b in bounds:
        result += struct.pack('>iiiiHHhh',
                              b.upper, b.lower, b.upper2, b.lower2,
                              b.bound_id, b.mp_cam_zoom, b.upper3, b.lower3)
    return bytes(result)


def _parse_backgrounds(data, off, sz):
    """Parse Background entries (24 bytes each)."""
    bgs = []
    count = sz // 24
    for i in range(count):
        p = off + i * 24
        raw = data[p:p + 24]
        # Parse: xBhhhhHHHxxxBxxxx → bg_id, xscroll, yscroll, ypos, xpos, bg1, bg2, bg3, zoom, unk
        bid = 0
        xscr = struct.unpack_from('>xBh', raw, 0)
        bg = Background()
        bg.bg_id = raw[1]
        bg.x_scroll = struct.unpack_from('>h', raw, 2)[0]
        bg.y_scroll = struct.unpack_from('>h', raw, 4)[0]
        bg.y_pos = struct.unpack_from('>h', raw, 6)[0]
        bg.x_pos = struct.unpack_from('>h', raw, 8)[0]
        bg.bg1 = struct.unpack_from('>H', raw, 10)[0]
        bg.bg2 = struct.unpack_from('>H', raw, 12)[0]
        bg.bg3 = struct.unpack_from('>H', raw, 14)[0]
        bg.zoom = struct.unpack_from('>I', raw, 16)[0]
        bg.unk = struct.unpack_from('>I', raw, 20)[0]
        bgs.append(bg)
    return bgs


def _ser_backgrounds(bgs: List[Background]) -> bytes:
    """Serialize Background entries (24 bytes each)."""
    result = bytearray()
    for bg in bgs:
        raw = bytearray(24)
        raw[1] = bg.bg_id & 0xFF
        struct.pack_into('>h', raw, 2, bg.x_scroll)
        struct.pack_into('>h', raw, 4, bg.y_scroll)
        struct.pack_into('>h', raw, 6, bg.y_pos)
        struct.pack_into('>h', raw, 8, bg.x_pos)
        struct.pack_into('>H', raw, 10, bg.bg1)
        struct.pack_into('>H', raw, 12, bg.bg2)
        struct.pack_into('>H', raw, 14, bg.bg3)
        struct.pack_into('>I', raw, 16, bg.zoom)
        struct.pack_into('>I', raw, 20, bg.unk)
        result += raw
    return bytes(result)


def _ser_entrances(ents: List[Entrance]) -> bytes:
    """Serialize Block 7: 20 bytes each."""
    result = bytearray()
    for e in ents:
        result += struct.pack('>HHHHBBBBxBBBHBB',
                              e.x, e.y, e.unk1, e.unk2,
                              e.entrance_id, e.dest_area, e.dest_entrance,
                              e.etype, e.zone_id, e.layer, e.path,
                              e.settings, e.leave_level, e.cp_direction)
    return bytes(result)


def _ser_sprites(sprites: List[Sprite]) -> bytes:
    """Serialize Block 8: 16 bytes each + FFFFFFFF terminator."""
    result = bytearray()
    for s in sprites:
        result += struct.pack('>HHH', s.stype, s.x, s.y)
        sd = s.spritedata
        if len(sd) < 6:
            sd = sd + b'\x00' * (6 - len(sd))
        result += sd[:6]
        result += struct.pack('>BBxx', s.zone_id, s.extra_byte)
    result += struct.pack('>I', 0xFFFFFFFF)
    return bytes(result)


def _ser_loaded_sprites(types: List[int]) -> bytes:
    """Serialize Block 9: 4 bytes each (u16 + pad)."""
    result = bytearray()
    for t in types:
        result += struct.pack('>Hxx', t)
    return bytes(result)


def _ser_zones(zones: List[Zone]) -> bytes:
    """Serialize Block 10: 24 bytes each."""
    result = bytearray()
    for z in zones:
        result += struct.pack('>HHHHHHBBBBxBBBBxBB',
                              z.x, z.y, z.w, z.h,
                              z.model_dark, z.terrain_dark,
                              z.zone_id, z.bound_id,
                              z.cam_mode, z.cam_zoom,
                              z.visibility, z.bg_a, z.bg_b,
                              z.cam_track, z.music, z.sfx)
    return bytes(result)


def _ser_locations(locs: List[Location]) -> bytes:
    """Serialize Block 11: 12 bytes each."""
    result = bytearray()
    for loc in locs:
        result += struct.pack('>HHHHBxxx', loc.x, loc.y, loc.w, loc.h, loc.loc_id)
    return bytes(result)


def _ser_paths(paths: List[Path]) -> bytes:
    """Serialize Block 13: 8 bytes each."""
    result = bytearray()
    for p in paths:
        result += struct.pack('>BBHHH', p.path_id, p.unk1, p.start_node, p.node_count, p.unk2)
    return bytes(result)


def _ser_path_nodes(nodes: List[PathNode]) -> bytes:
    """Serialize Block 14: 16 bytes each."""
    result = bytearray()
    for n in nodes:
        result += struct.pack('>HHffhxx', n.x, n.y, n.speed, n.accel, n.delay)
    return bytes(result)
