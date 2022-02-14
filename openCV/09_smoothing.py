import cv2 as cv
import numpy as np

img = cv.imread('openCV/glass.jpg')
cv.imshow('Glass', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# More Blur
average = cv.blur(img, (7,7))
cv.imshow('More Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 1)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 51, 51)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
