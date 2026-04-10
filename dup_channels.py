"""
Convert 4ch menu WAV to 8ch by duplicating the channels.
NSMBW menu uses 8 channels:
  Ch 0-3: TV mix (L, R, rear L, rear R)
  Ch 4-7: Wiimote speaker mix (same as TV for our purposes)
We duplicate channels 0-3 as 4-7.
"""
import wave
import struct
import array

INPUT = 'temp_menu_4ch.wav'
OUTPUT = 'temp_menu_8ch.wav'

# Read 4ch WAV
with wave.open(INPUT, 'rb') as wf:
    n_channels = wf.getnchannels()
    sample_width = wf.getsampwidth()
    framerate = wf.getframerate()
    n_frames = wf.getnframes()
    raw_data = wf.readframes(n_frames)

print(f"Input: {n_channels}ch, {sample_width*8}bit, {framerate}Hz, {n_frames} frames")
print(f"Raw data size: {len(raw_data)} bytes")

if n_channels != 4:
    print(f"WARNING: Expected 4 channels, got {n_channels}")

# Each frame is: [ch0_sample, ch1_sample, ch2_sample, ch3_sample]
# We need: [ch0, ch1, ch2, ch3, ch0, ch1, ch2, ch3]
# i.e. duplicate each 4-channel frame as 8-channel frame

bytes_per_sample = sample_width
bytes_per_frame_in = n_channels * bytes_per_sample
bytes_per_frame_out = 8 * bytes_per_sample

print(f"Bytes per input frame: {bytes_per_frame_in}")
print(f"Bytes per output frame: {bytes_per_frame_out}")
print(f"Estimated output size: {n_frames * bytes_per_frame_out} bytes")

# Process in chunks for memory efficiency
out_data = bytearray()
for i in range(n_frames):
    offset = i * bytes_per_frame_in
    frame_4ch = raw_data[offset:offset + bytes_per_frame_in]
    # Duplicate: 4ch frame becomes 8ch by repeating
    out_data.extend(frame_4ch)  # channels 0-3
    out_data.extend(frame_4ch)  # channels 4-7 (duplicate)

print(f"Output data size: {len(out_data)} bytes")

# Write 8ch WAV
with wave.open(OUTPUT, 'wb') as wf:
    wf.setnchannels(8)
    wf.setsampwidth(sample_width)
    wf.setframerate(framerate)
    wf.writeframes(bytes(out_data))

print(f"Written {OUTPUT}: 8ch, {sample_width*8}bit, {framerate}Hz, {n_frames} frames")
