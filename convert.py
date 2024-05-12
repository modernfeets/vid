import os
import subprocess

def convert_to_m3u8(input_file, output_dir):
    output_file = os.path.join(output_dir, "output.m3u8")
    command = [
        'ffmpeg',
        '-i', input_file,
        '-profile:v', 'baseline',
        '-level', '3.0',
        '-s', '640x360',  # Change resolution as needed
        '-start_number', '0',
        '-hls_time', '10',
        '-hls_list_size', '0',
        '-f', 'hls',
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Conversion of {input_file} successful.")
    except subprocess.CalledProcessError as e:
        print(f"Conversion of {input_file} failed:", e)

if __name__ == "__main__":
    # Input and output directories
    input_dir = "videos"
    output_base_dir = "vid"

    # Create the output base directory if it doesn't exist
    os.makedirs(output_base_dir, exist_ok=True)

    # Iterate over all .mp4 files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_dir, filename)
            output_dir = os.path.join(output_base_dir, os.path.splitext(filename)[0])
            os.makedirs(output_dir, exist_ok=True)
            convert_to_m3u8(input_file, output_dir)
