import sys

def calculate_fast_loop(original_loop_start, original_total_samples, speed_multiplier):
    """
    Calculates the new loop points when you speed up a song by a multiplier.
    For Mario games, the "Fast" version is usually exactly 1.15x or 1.25x faster.
    """
    new_loop_start = int(original_loop_start / speed_multiplier)
    new_total_samples = int(original_total_samples / speed_multiplier)
    
    print(f"--- Fast Version Math (Speed: {speed_multiplier}x) ---")
    print(f"Original Loop Start : {original_loop_start} -> NEW Loop Start: {new_loop_start}")
    print(f"Original Total      : {original_total_samples} -> NEW Total:      {new_total_samples}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python calc_fast_loop.py <original_loop_start> <original_total_samples> <speed_multiplier>")
        print("Example: python calc_fast_loop.py 737600 2890135 1.15")
    else:
        loop_start = int(sys.argv[1])
        total = int(sys.argv[2])
        mult = float(sys.argv[3])
        calculate_fast_loop(loop_start, total, mult)
