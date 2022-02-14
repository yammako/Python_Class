import cv2 as cv
import numpy as np

img = cv.imread('openCV/glass.jpg')

cv.imshow('Glass', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found for Canny!')
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn for Canny', blank)


# Reduce the contours
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

contours, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found for Blur!')
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn for Blur', blank)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny with Blur', canny)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found for Canny Blur!')
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn for Canny Blur', blank)

ret, thresh = cv.threshold(gray, 220, 255, cv.THRESH_BINARY)    # 220 --> 0, 255 --> 255 Binary image
cv.imshow('Thresh', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found for Threshold!')
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn for Threshold', blank)

cv.waitKey(0)