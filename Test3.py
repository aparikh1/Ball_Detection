from __future__ import print_function

import io
import time
import picamera
import cv2
import numpy as np
import sys


def nothing(*arg):
	pass

cv2.namedWindow('edge')
cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

#
#Capture video to stream
stream=io.BytesIO()
camera=picamera.PiCamera()

camera.resolution=(640, 480)
camera.hflip=True
camera.vflip=True
#camera.start_preview()
time.sleep(0.1)
camera.capture(stream, format='jpeg')

while True:
	

	data=np.fromstring(stream.getvalue(), dtype=np.uint8)
	image=cv2.imdecode(data, 1)
#	gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#	thrs1=cv2.getTrackbarPos('thrs1', 'edge')
#	thrs2=cv2.getTrackbarPos('thrs2', 'edge')
#	edge=cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
#	vis=image.copy()
#	vis=np.uint8(vis/2.)
#	vis[edge != 0] = (0, 255, 0)
	cv2.imshow('edge', image)

	ch=cv2.waitKey(5) &0xFF
	if ch==27:
		break
camera.close()
cv2.destroyAllWindows()
