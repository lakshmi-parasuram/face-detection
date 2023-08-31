# plot photo with detected faces using opencv cascade classifier
from cv2 import imshow
from cv2 import waitKey
from cv2 import imread
from cv2 import destroyAllWindows
from cv2 import rectangle
from cv2 import CascadeClassifier
# read the image in pixels
pixels = imread('../../data/family.jpg')
# load the CascadeClassifier existing model
cascadeClassifier = CascadeClassifier('config.xml')
# here is where we do the face detection
bboxes = cascadeClassifier.detectMultiScale(pixels)
# for each face detected draw the boundaries
for box in bboxes:
	x, y, width, height = box
	x2, y2 = x + width, y + height
	# overlaying a red rectangle
	rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
# open a window and show the faces detected
imshow('face detection', pixels)
# the window will be open until we press any key
waitKey(0)
# close the image window showing faces detected
destroyAllWindows()