import numpy as np
import cv2
import glob
import math
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9*18,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:18].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

img_checkerboard = cv2.imread("../data/pattern1_25mm_3m.png",0)



img_pattern3 = cv2.imread("../data/pattern3_25mm_3m.png",0)
img_pattern4 = cv2.imread("../data/pattern4_25mm_3m.png",0)
img_pattern5 = cv2.imread("../data/pattern5_25mm_3m.png",0)
img_pattern6 = cv2.imread("../data/pattern6_25mm_3m.png",0)


# gray_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
# gray_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
# gray_back = cv2.cvtColor(img_back,cv2.COLOR_BGR2GRAY)
gray_1 = img_checkerboard

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(img_checkerboard, (8,16),cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE)
# If found, add object points, image points (after refining them)
print corners
if ret == True:
    objpoints.append(objp)

    corners2 = cv2.cornerSubPix(img_checkerboard,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)

    # Draw and display the corners
    cv2.namedWindow("checkerboard")
    img = cv2.drawChessboardCorners(img_checkerboard, (8,16), corners2,ret)
    cv2.imshow('checkerboard',img)
    # cv2.namedWindow("pattern3")
    # img = cv2.drawChessboardCorners(img_pattern3, (8,16), corners2,ret)
    # cv2.imshow('pattern3',img)
    # cv2.namedWindow("pattern4")
    # img = cv2.drawChessboardCorners(img_pattern4, (8,16), corners2,ret)
    # cv2.imshow('pattern4',img)
    # cv2.namedWindow("pattern5")
    # img = cv2.drawChessboardCorners(img_pattern5, (8,16), corners2,ret)
    # cv2.imshow('pattern5',img)
    # cv2.namedWindow("pattern6")
    # img = cv2.drawChessboardCorners(img_pattern6, (8,16), corners2,ret)
    # cv2.imshow('pattern6',img)
    # cv2.waitKey(0)
cv2.destroyAllWindows()
img_here  = img_pattern5

dst_x = cv2.Sobel(img_here, cv2.CV_64F, 0, 1, scale=3)
dst_y = cv2.Sobel(img_here, cv2.CV_64F, 1, 0, scale=3)
print img_pattern3.shape



for i in range(corners.shape[0]):
# for i in range(2):
	# print corners.shape
	# print corners[i][0]
	# print dst_x.shape
	# print dst_x[int(corners[i][0][1])][int(corners[i][0][0])]
	# print dst_y[int(corners[i][0][1])][int(corners[i][0][0])

	x = dst_x[int(corners[i][0][1])][int(corners[i][0][0])]
	y = dst_y[int(corners[i][0][1])][int(corners[i][0][0])]
	theta = 0.0
	theta_x = 0.0
	theta_y = 0.0
	for u in range(3):
		for v in range(3):
				x_temp = dst_x[int(corners[i][0][1])+u -1 ][int(corners[i][0][0]) + v -1]
				y_temp = dst_y[int(corners[i][0][1])+u -1 ][int(corners[i][0][0]) + v -1]
				# print "x = ",x_temp
				# print "y =", y_temp
				# if(y_temp != 0):
					# theta_temp = math.atan2(y_temp,x_temp)
					# print "theta_ttemp = ", theta_temp*180/np.pi
					# theta = theta + theta_temp / 9
				theta_x = theta_x + x_temp
				theta_y = theta_y + y_temp
	theta = math.atan2(theta_y,theta_x)
	print "theta_x = ", theta_x
	print "theta_y = ", theta_y
	print "theta = ",theta
	# theta = np.arctan2(y,x)

	# print theta
	# print int(corners[i][0][0]+np.sin(theta)*5)
	# print int(corners[i][0][0]+np.cos(theta)*5)
	# img = cv2.line(img_pattern3,(corners[i][0][1],corners[i][0][0]),(int(corners[i][0][1]+np.sin(theta)*1000),int(corners[i][0][0]+np.cos(theta)*1000)),(255,0,0),50)
	img = cv2.line(img_here,(corners[i][0][0],corners[i][0][1]),(int(corners[i][0][0]+np.sin(theta)*20),int(corners[i][0][1]+np.cos(theta)*20)),(254,0,0),1)
cv2.namedWindow("derative")
cv2.imshow('derative',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()