import cv2 as cv
import numpy as np

img = cv.imread('openCV/glass.jpg')

cv.imshow('Glass', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
    # -x --> Left
    # -y --> Up
    # x --> Right
    # y --> Down

translated = translate(img, 100, 100)
cv.imshow('Translate to Right and Down', translated)

translated = translate(img, -100, -100)
cv.imshow('Translate to Left and Up', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated with counter-clockwise', rotated)

rotated = rotate(img, -45)
cv.imshow('Rotated with clockwise', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated with clockwise', rotated_rotated)

rotated_90 = rotate(img, -90)
cv.imshow('Rotated 90', rotated_90)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping (0: Vertical, 1: Horizontal, -1: Both)
flip = cv.flip(img, 0)
cv.imshow('Flip with 0', flip)

flip = cv.flip(img, 1)
cv.imshow('Flip with 1', flip)

flip = cv.flip(img, -1)
cv.imshow('Flip with -1', flip)

rotated_180 = rotate(img, -180)
cv.imshow('Rotated 180', rotated_180)

# Cropping
cropped = img[200:400, 300:500]
cv.imshow('Cropped', cropped)
cv.waitKey(0)