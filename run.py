from pytube import YouTube
import os

def download_video(url, output_dir, filename):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_dir, filename=filename)

        print(f"Downloaded {filename}.mp4 successfully!")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    # Create the output directory if it doesn't exist
    output_dir = "videos"
    os.makedirs(output_dir, exist_ok=True)

    # Read URLs from list.txt
    with open("list.txt", "r") as file:
        urls = file.readlines()

    # Download each video
    for i, url in enumerate(urls):
        url = url.strip()
        filename = f"{i+1}.mp4"
        download_video(url, output_dir, filename)
