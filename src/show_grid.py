import numpy as np
import cv2

img1 = cv2.imread('pattern3.png',cv2.IMREAD_COLOR )
img2 = cv2.imread('pattern4.png',cv2.IMREAD_COLOR )
img3 = cv2.imread('pattern5.png',cv2.IMREAD_COLOR )
img4 = cv2.imread('pattern6.png',cv2.IMREAD_COLOR )
img5 = cv2.imread('pattern1.png',cv2.IMREAD_COLOR )
while(1):
	cv2.imshow('image',img5)
	cv2.waitKey(0)
	cv2.imshow('image',img1)
	cv2.waitKey(0)
	cv2.imshow('image',img2)
	cv2.waitKey(0)
	cv2.imshow('image',img3)
	cv2.waitKey(0)
	cv2.imshow('image',img4)
	cv2.waitKey(0)
cv2.destroyAllWindows()


	
