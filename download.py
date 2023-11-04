# Import the Pytube library, which allows us to work with YouTube videos.
from pytube import YouTube

# Specify the URL of the YouTube video that we want to download.
video_link = "Youtube video link"

# Create a 'YouTube' object by providing the video link.
yt = YouTube(video_link)

# Use the 'yt.streams.first().download()' method to download the video.
# This line fetches the best available quality stream and starts the download.
yt.streams.first().download()