# youtube_playlist_download_python
This Python script is used to download videos from a YouTube playlist.

# How to Run this script:

> You will need to install the following package in your system to follow the next steps.

- pip
- python > 3.8
- very good internet connection

then, run the following command in terminal;

- pip3 install -r requirements.txt

now run the script using the following command;

- python3 main.py

it will ask for the playlist url; simply paste it and then downloading will starts...



# let's understand the script.
First, the script imports the `os` module for creating a new folder, and the `Playlist` class from the `pytube` module for accessing and downloading videos from the YouTube playlist.

The `make_alpha_numeric` function is defined to remove any non-alphanumeric characters from a given string.

The script prompts the user to enter a YouTube playlist URL and stores it in the `link` variable.

Then, an instance of the `Playlist` class is created using the `link`.

The title of the playlist is extracted and passed to the `make_alpha_numeric` function to ensure it is a valid folder name. The resulting alphanumeric string is stored in the `folderName` variable.

The script then tries to create a new folder using the `os.mkdir` function with the `folderName` as the folder name. If an exception occurs, it is caught and an error message is printed.

The total number of videos in the playlist is calculated using the `len` function on `yt_playlist.videos` and stored in the `totalVideoCount` variable.

A loop is executed for each video in the playlist using the `enumerate` function with `yt_playlist.videos` as the iterable, and `index` as the starting value. This loop allows the script to keep track of the current video's index in the playlist.

Within the loop, each video's title is printed, and the size of the highest resolution stream is determined using `video.streams.get_highest_resolution().filesize`. The size is then converted from bytes to megabytes and printed.

The highest resolution stream is downloaded using `video.streams.get_highest_resolution().download(output_path=folderName)`, specifying the output folder using the `output_path` parameter.

If the download is successful, a success message is printed along with the remaining number of videos to be downloaded.

If any exception occurs during the download process, an error message is printed.

Finally, a success message is printed once all the videos have been downloaded.

This script makes use of the `pytube` library to interact with YouTube and download videos, and the `os` module to create the necessary folders.