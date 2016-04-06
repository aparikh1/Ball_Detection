from __future__ import print_function
import sys
import numpy as np
import cv2

def find_marker(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	cnts=cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

	c=max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	radius = radius * 2
	
	return (radius)

def distance_to_cam(knownWidth, focalLength, perWidth):
	return(knownWidth * focalLength)/perWidth


knownDist=17.0
Width=2.228


#Image_Path = ["amit/ball.png"]

#image=cv2.imread(Image_Path[0])
#marker = find_marker(image)
fLength=398.125

try:
	fn = int(sys.argv[1])
except:
	fn = 1
cap=cv2.VideoCapture(fn)

ret, frame=cap.read()

marker = find_marker(frame)

#fLength = (marker * knownDist)/Width

inches=distance_to_cam(Width, fLength, marker)
print(inches)

#	cv2.putText(frame, "%.2fft" % (inches), (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
while True:
	cv2.imshow("Image", frame)

	ch=cv2.waitKey(5) &0xFF
	if (ch==27):
		break

cap.release()
cv2.destroyAllWindows()




