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

for foo in camera.capture_continuous(stream, format='jpeg'):
	stream.truncate()
	stream.seek(0)	
	
	#Convert to OpenCV Object
	data=np.fromstring(stream.getvalue(), dtype=np.uint8)
	src=cv2.imdecode(data, 1)
	
	#Convert to grayscale
	img=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	
	#Blur image
	img=cv2.medianBlur(img, 5)
	cimg=src.copy()

	#Run Hough transform
	#cv2.HoughCircles(image, method, ratio of image resolution to accumulator resolution, min dist btwn circles, output vector of circles, higher threshold for edge detection, accumulator threshold, min radius, max radius)
	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)

	if circles is not None:	#If circles are detected
		circles=np.round(circles[0,:]).astype("int")
		
		for (x, y, r) in circles:
			cv2.circle(cimg,(x, y), r, (0, 0, 255), 4)	#edge of circle
			cv2.circle(cimg, (x, y), 2, (0, 255, 0), 4)	#center of circle
			cv2.imshow("source", src)
			cv2.imshow("detected circles", cimg)

	ch=cv2.waitKey(5) &0xFF
	if ch==27:
		break
camera.close()
cv2.destroyAllWindows()
