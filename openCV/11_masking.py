import cv2 as cv
import numpy as np

img = cv.imread('openCV/glass.jpg')
cv.imshow('Glass', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

# Circle mask
mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle Mask', mask)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Circle Masked Image', masked)

# Rectangle mask
mask1 = cv.rectangle(blank.copy(), (100,100), (500,500), 255, -1)
cv.imshow('Rectangle Mask', mask1)
masked1 = cv.bitwise_and(img,img,mask=mask1)
cv.imshow('Rectangle Masked Image', masked1)
cv.waitKey(0)