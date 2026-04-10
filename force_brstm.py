import os
import sys
import struct

def force_brstm_headers(filepath, new_channels, new_sample_rate, loop_start):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    print(f"Forcing headers for {os.path.basename(filepath)}...")
    
    with open(filepath, "r+b") as f:
        magic = f.read(4)
        if magic != b'RSTM':
            print("Error: This is not a standard Wii RSTM file. Please convert from 3DS/WiiU first.")
            return
            
        f.seek(0x10)
        head_offset = struct.unpack(">I", f.read(4))[0]
        
        f.seek(head_offset + 0x08)
        stream_info_ref_offset = struct.unpack(">I", f.read(4))[0]
        stream_info_start = head_offset + stream_info_ref_offset
        
        # Overwrite Channels
        f.seek(stream_info_start + 0x01)
        f.write(struct.pack("B", 1)) # Force Loop Flag to 1 (True)
        f.write(struct.pack("B", new_channels)) # Overwrite channels
        print(f" -> Forced channels to {new_channels}")
        print(f" -> Forced loop flag to True")
        
        # Overwrite Sample Rate
        f.seek(stream_info_start + 0x04)
        f.write(struct.pack(">H", new_sample_rate))
        print(f" -> Forced sample rate to {new_sample_rate}Hz")
        
        # Overwrite Loop Start
        if loop_start > 0:
            f.seek(stream_info_start + 0x08)
            f.write(struct.pack(">I", loop_start))
            print(f" -> Forced loop start to {loop_start} samples")

    print(f"Finished forcing headers. Try playing it in-game now.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python force_brstm.py <path>")
    else:
        # For the menu, force 4 channels, 32000Hz, loop at sample 100000
        force_brstm_headers(sys.argv[1], 4, 32000, 100000)
