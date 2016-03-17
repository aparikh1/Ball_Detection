from __future__ import print_function

import io
import time
import picamera
import cv2
import numpy as np

import sys

#
#Capture video to stream
stream=io.BytesIO()
camera=picamera.PiCamera()

camera.resolution=(640, 480)
camera.hflip=True
camera.vflip=True
#camera.start_preview()
#time.sleep(0.1)
#camera.capture(stream, format='jpeg')

#while True:
for foo in camera.capture_continuous(stream, format='jpeg'):
	stream.truncate()
	stream.seek(0)	

	data=np.fromstring(stream.getvalue(), dtype=np.uint8)
	src=cv2.imdecode(data, 1)
	img=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	img=cv2.medianBlur(img, 5)
	cimg=src.copy()

	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)

#	a, b, c = circles.shape
#	for i in range(b):
#		cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
#       	cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)  # draw center of circle
	if circles is not None:
		circles=np.round(circles[0,:]).astype("int")
		
		for (x, y, r) in circles:
			cv2.circle(cimg,(x, y), r, (0, 0, 255), 4)
			cv2.circle(cimg, (x, y), 2, (0, 255, 0), 4)
			cv2.imshow("source", src)
			cv2.imshow("detected circles", cimg)

	ch=cv2.waitKey(5) &0xFF
	if ch==27:
		break
camera.close()
cv2.destroyAllWindows()