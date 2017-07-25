import numpy as np
import cv2
import glob
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9*18,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:18].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

img_checkerboard = cv2.imread("../data/pattern1_25mm_3m.png",0)



img_patern3 = cv2.imread("../data/pattern3_25mm_3m.png",0)
img_patern4 = cv2.imread("../data/pattern4_25mm_3m.png",0)
img_patern5 = cv2.imread("../data/pattern5_25mm_3m.png",0)
img_patern6 = cv2.imread("../data/pattern6_25mm_3m.png",0)


# gray_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
# gray_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
# gray_back = cv2.cvtColor(img_back,cv2.COLOR_BGR2GRAY)
gray_1 = img_checkerboard

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(img_checkerboard, (8,16),cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE)
# If found, add object points, image points (after refining them)
if ret == True:
    objpoints.append(objp)

    corners2 = cv2.cornerSubPix(img_checkerboard,corners,(11,11),(-1,-1),criteria)
    imgpoints.append(corners2)

    # Draw and display the corners
    cv2.namedWindow("checkerboard")
    img = cv2.drawChessboardCorners(img_checkerboard, (8,16), corners2,ret)
    cv2.imshow('checkerboard',img)
    cv2.namedWindow("pattern3")
    img = cv2.drawChessboardCorners(img_patern3, (8,16), corners2,ret)
    cv2.imshow('pattern3',img)
    cv2.namedWindow("pattern4")
    img = cv2.drawChessboardCorners(img_patern4, (8,16), corners2,ret)
    cv2.imshow('pattern4',img)
    cv2.namedWindow("pattern5")
    img = cv2.drawChessboardCorners(img_patern5, (8,16), corners2,ret)
    cv2.imshow('pattern5',img)
    cv2.namedWindow("pattern6")
    img = cv2.drawChessboardCorners(img_patern6, (8,16), corners2,ret)
    cv2.imshow('pattern6',img)
    cv2.waitKey(0)
  
cv2.destroyAllWindows()
