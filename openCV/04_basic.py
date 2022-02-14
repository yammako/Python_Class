import cv2 as cv

img = cv.imread('openCV/glass.jpg')

cv.imshow('Glass', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Reduced Edge
canny = cv.Canny(blur, 125, 175)
cv.imshow('Reduced Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated with iter 3', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized Image', resized)

resized = cv.resize(img, (2000,1500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image1', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)