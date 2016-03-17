from __future__ import print_function
import io
import time
import picamera
import cv2
import numpy as np

blueLower=(100, 0, 0)
blueUpper=(150, 255, 255)

camera=picamera.PiCamera()
stream=io.BytesIO()

camera.resolution=(640,480)
camera.hflip=True
camera.vflip=True

for foo in camera.capture_continuous(stream, format='jpeg'):
	stream.truncate()
	stream.seek(0)
	
	data=np.fromstring(stream.getvalue(), dtype=np.uint8)
	image=cv2.imdecode(data, 1)

	hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv, blueLower, blueUpper)

	cv2.imshow('image', mask)

	ch=cv2.waitKey(5) &0xFF
	if ch==27:
		break

camera.close()
cv2.destroyAllWindows