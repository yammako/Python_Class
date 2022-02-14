import cv2 as cv
import numpy as np

img = cv.imread('openCV/glass.jpg')
cv.imshow('Glass', img)

b,g,r = cv.split(img)       # split color channels with sequence B, G, and R

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# print dimensions of each color channel
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge color channels
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)
print(merged.shape)

# B, G, R image generation
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue Image', blue)
cv.imshow('Green Image', green)
cv.imshow('Red Image', red)

cv.waitKey(0)