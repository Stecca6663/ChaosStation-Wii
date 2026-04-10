import wave
import os
import sys

def duplicate_to_4_channels(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    try:
        with wave.open(input_path, 'rb') as w_in:
            params = w_in.getparams()
            
            if params.nchannels != 2:
                print(f"Error: Source file has {params.nchannels} channels. This script only supports 2-channel (stereo) WAV files.")
                return

            print(f"Reading {os.path.basename(input_path)}...")
            print(f" - Sample Rate: {params.framerate}Hz")
            print(f" - Sample Width: {params.sampwidth} bytes")
            
            # Create 4-channel params
            new_params = list(params)
            new_params[0] = 4 # nchannels
            
            with wave.open(output_path, 'wb') as w_out:
                w_out.setparams(tuple(new_params))
                
                # Processing in chunks to be memory efficient
                chunk_size = 1024 * 16
                for _ in range(0, params.nframes, chunk_size):
                    frames = w_in.readframes(chunk_size)
                    if not frames:
                        break
                    
                    # Each frame for 16-bit stereo is 4 bytes (2 for L, 2 for R)
                    # We want to turn [L][R] into [L][R][L][R]
                    frame_size = 2 * params.sampwidth
                    new_frames = bytearray()
                    
                    for i in range(0, len(frames), frame_size):
                        sample_pair = frames[i : i + frame_size]
                        new_frames.extend(sample_pair) # Front L/R
                        new_frames.extend(sample_pair) # Back L/R (Duplicated)
                    
                    w_out.writeframes(new_frames)
                    
            print(f"Successfully created: {output_path}")
            print("You can now use this 4-channel WAV in BrawlCrate's 'Replace' menu.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python duplicate_channels.py input.wav output_4ch.wav")
    else:
        duplicate_to_4_channels(sys.argv[1], sys.argv[2])
