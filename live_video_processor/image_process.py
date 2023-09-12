import cv2

# here providing an example url used for testing
url = 'http://localhost:3000/html/cam_pic_new.php?time=1732862568010&p'
videocapture = cv2.VideoCapture(url)

cv2.namedWindow('live streaming video', cv2.WINDOW_NORMAL)

while(True):
    newFrame, image = videocapture.read()
    #img_resize = cv2.resize(frame, (960, 540))
    # cv2.imshow('live streaming', frame)
    if newFrame:
        # Actually writing the image to output jpg file
        cv2.imwrite("image" + str(count) + ".jpg", image)
    # if the streaming is stopped and could not retrive further images
    # quit and break the image
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

videocapture.release()
cv2.destroyAllWindows()