import os
import yt_dlp

def download_youtube_playlist(playlist_url, download_path):
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Define download options
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save files with title as name
        'noplaylist': False,  # Ensure the entire playlist is downloaded
    }

    # Download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    # URL of the YouTube playlist
    playlist_url = input("Enter the playlist URL: ")

    # Directory where you want to save the videos
    download_path = input("Enter the download directory path: ")

    # Download the playlist
    download_youtube_playlist(playlist_url, download_path)
