from __future__ import print_function
import sys
import numpy as np
import cv2

blueLower=(110, 64, 40)
blueUpper=(130, 255, 170)

try:
	fn = int(sys.argv[1])
except:
	fn = 1
cap=cv2.VideoCapture(fn)

while True:
	ret, frame=cap.read()
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv, blueLower, blueUpper)

#	cv2.imshow('image',mask)

	cnts=cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center=None

	if len(cnts)>0:
		c=max(cnts, key=cv2.contourArea)
		((x,y),radius)=cv2.minEnclosingCircle(c)
		M=cv2.moments(c)
		center=(int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
		
		if radius>10:
			cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

	cv2.imshow("Frame", frame)
	print(center)

	ch=cv2.waitKey(5) &0xFF
	if (ch==27):
		break

cv2.destroyAllWindows()
