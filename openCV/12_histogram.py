import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('openCV/glass.jpg')
cv.imshow('Glass', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

img = cv.imread('openCV/Koala.jpg')
cv.imshow('Koala', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Koala', gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram1')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('Masked', masked)
gray_hist_mask = cv.calcHist([masked], [0], None, [256], [0, 256])
plt.figure()
plt.title('Masked Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist_mask)
plt.xlim([0,256])
plt.show()


# Color image histogram
plt.figure()
plt.title('Color image Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')

colors = ('Blue', 'Green', 'Red')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=colors[i])
    plt.xlim([0,256])

plt.legend()
plt.show()

cv.waitKey(0)