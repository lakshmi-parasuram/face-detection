import requests
from pydub import AudioSegment

# from the streaming url
url = "http://localhost:3000/html/cam_pic_new.php?time=1732862568010&p"
response = requests.get(url, stream=True)

# download and save it as mp4 file
with open("video.mp4", 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# Load the video file
video = AudioSegment.from_file("video.mp4", format="mp4")

# Export the audio file using pydub
video.export("interview.mp3", format="mp3")

# now we need to call diarization pipeline from our code