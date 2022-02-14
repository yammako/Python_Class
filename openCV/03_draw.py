import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image a certain color
blank[:] = 0, 255, 0        # BGR
cv.imshow('Green', blank)

blank[:] = 255, 0, 0        # BGR
cv.imshow('Blue', blank)

blank[:] = 0, 0, 255        # BGR
cv.imshow('Red', blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Part of Green', blank)

# Draw a Rectangle
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle Filled', blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle Filled by -1', blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle with Quarter size', blank)

# Draw a Circle
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle Filled', blank)

# Draw a Line
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.line(blank, (100,100), (200,150), (255,255,255), thickness=3)
cv.imshow('Line1', blank)

# Write Text
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.putText(blank, 'Hello, my name is Cho.', (50, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)