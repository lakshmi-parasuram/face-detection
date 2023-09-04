import cv2
import moviepy
videocapture = cv2.VideoCapture('interview.mp4')

def getImageFrame(sec):
    videocapture.set(cv2.CAP_PROP_POS_MSEC,sec * 1000)
    # Reading the image and the 
    newFrame, image = videocapture.read()
    if newFrame:
        # Actually writing the image to output jpg file
        cv2.imwrite("image" + str(count) + ".jpg", image)
    return newFrame


def getAudio():
    video = moviepy.editor.VideoFileClip("interview.mp4")
    audio = video.audio
    audio.write_audiofile("Interview.mp3")
    return


sec = 0
# the frame rate at interval to take the images from video sample
frameRate = 1
count = 1
success = getImageFrame(sec)

# Loop untill there are no frames available from the video
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getImageFrame(sec)

getAudio()