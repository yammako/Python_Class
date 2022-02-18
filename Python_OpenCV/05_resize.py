# 크기 조정
# 고정 크기 설정
import cv2 as cv

img = cv.imread('openCV/glass.jpg')
dst = cv.resize(img, (800, 500))
cv.imshow('Original', img)
cv.imshow('Resize', dst)

# 비율 크기 설정
dst1 = cv.resize(img, None, fx = 0.5, fy = 0.5)     # 0.5배로 크기 조절
cv.imshow('Resize with ratio', dst1)

# 크기 조절에 사용되는 보간법 (interpolation)
# cv.INTER_AREA: 크기를 줄일 때 사용
# cv.INTER_CUBIC: 크기를 늘릴 때 사용 (속도가 느림)
# cv.INTER_LINEAR: 크기를 늘릴 때 사용 (Default)
dst2 = cv.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)     # 0.5배로 크기 조절
dst3 = cv.resize(dst2, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)     # 2배로 크기 조절
dst4 = cv.resize(dst2, None, fx = 2, fy = 2, interpolation = cv.INTER_LINEAR)     # 2배로 크기 조절

cv.imshow('Resize with AREA', dst2)
cv.imshow('Resize with CUBIC', dst3)
cv.imshow('Resize with LINEAR', dst4)

# 동영상 크기 조절
video = cv.VideoCapture('openCV/Piano.mp4')

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    frame1 = cv.resize(frame, (400, 500))    
    frame2 = cv.resize(frame, None, fx = 2, fy = 2, interpolation=cv.INTER_CUBIC)    
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame1)
    cv.imshow('Resized Video with CUBIC', frame2)
    if cv.waitKey(1) == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()
