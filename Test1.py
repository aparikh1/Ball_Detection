from __future__ import print_function
import sys
import numpy as np
import cv2

blueLower=(110, 64, 40)
blueUpper=(130, 255, 170)
#started with (100-150, 0-255, 0-255): this considered too many things to be in the range (100-200 was a very wide and arbitrary range); false positives on much of the image exluding about middle ~40%; black was usually considered false positive. 

#(105-130, ~, ~): did okay in solid backgrounds, however backgrounds with different shapes and contours, there were many false positive; black seemed to be recorded as a false positive alot also; in low light had far fewer false positives, however also struggled recognizing color of ball completely

#(110-130, ~, ~): much better at not counting black as false positive; weird contours still give it false positives; performs well in low light and well-lit areas; still false positives on fringes;

#(~,64-190,~): only recognized outline of ball, possible not inlcuding high saturation points?

#(~,64-255,~): recognized entire ball; did much better job of not giving false positives to weird contours; performs extremely well in well-lit area, but does not recongize ball in low-light; still recognizes black as false positives a little

#(~,~,128-255): did not recognize parts of the ball that were not well-lit; removed almost all black noise; need to recognize less bright colors

#(~,~,64-190): recognized most of the ball, however had problems recognizing extremeties that were not well lit; not much black noise, but a little bright noise

#(~,~,40-153): recognizes most of ball, however now cannot detect parts of ball that have glare; does well in well-lit and moderately lit areas;

#(~,~,40-170): recognizes ball very well, despite glare. can recongize against solid backgrounds about 4 feet away, and against other backgrounds almost 3 feet away.

try:
	fn = int(sys.argv[1])
except:
	fn = 0
cap=cv2.VideoCapture(fn)

while True:
	ret, frame=cap.read()
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv, blueLower, blueUpper)

	cv2.imshow('image',mask)

	ch=cv2.waitKey(5) &0xFF
	if (ch==27):
		break

cv2.destroyAllWindows()
