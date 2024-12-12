import cv2 as cv
import numpy as np
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = (22.5 * np.mgrid[0:7,0:6]).T.reshape(-1,2)

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
cam = cv.VideoCapture("/home/zeyad/Downloads/calib.avi") #add path calibration video here
if cv.VideoCapture.isOpened(cam) :
    print("Camera found")
else:
    print("Camera not found")
    images = []
    frameno = 0
    while(frameno < 500):
       ret,frame = cam.read()
       if ret:
          # if video is still left continue creating images
          name = str(1) + '.jpg'
          frameno = frameno + 1
          cv.imwrite(name, frame)
          img = cv.imread(name)
          ############################3
          gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
          # Find the chess board corners
          ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    
          # If found, add object points, image points (after refining them)
          if ret == True:
            objpoints.append(objp)
    
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)
       else:
          break
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(np.array(mtx))