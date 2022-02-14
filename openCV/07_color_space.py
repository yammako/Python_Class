import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('openCV/glass.jpg')
cv.imshow('Glass', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV ---> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB ---> BGR', lab_bgr)

# HSV to LAB (Can't directly convert HSV to LAB. Should do HSV --> BGR --> LAB)
hsv_lab = cv.cvtColor(cv.cvtColor(hsv, cv.COLOR_HSV2BGR), cv.COLOR_BGR2LAB)
cv.imshow('HSV ---> LAB', hsv_lab)
# matplotlib.pyplot has RGB basis NOT BGR
# plt.imshow(img)           
# plt.show()
# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)