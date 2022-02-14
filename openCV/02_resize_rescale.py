import cv2 as cv                        # OpenCV 패키지 사용, cv2를 cv로 사용, OpenCV 패키지 내의 함수를 사용할 때 cv.을 먼저 쓰고 함수명을 써야 함.

# 이미지 크기 조절 함수 (사용자 정의)
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Read Image
img = cv.imread('openCV/large_dark_cave.jpg') # 아주 큰 해상도를 가지는 영상 입력
cv.imshow('Large Image', img)          # 모니터 해상도보다 커서 윈도우가 화면보다 더 큼.

img1 = rescaleFrame(img)
cv.imshow('Resized', img1)

img2 = rescaleFrame(img, scale=0.1)
cv.imshow('Resized1', img2)
cv.waitKey(0)                           # 어떠한 키 값을 받을 때까지 윈도우 종료하지 않음.


# Read Video
# capture = cv.VideoCapture(0)            # 카메라를 사용항 동영상 출력
# capture = cv.VideoCapture(1)            # 카메라를 사용항 동영상 출력
capture = cv.VideoCapture('openCV/Piano.mp4')  # 동영상 파일 출력

while True:
    isTrue, frame = capture.read()
    frame1 = rescaleFrame(frame)
    frame2 = rescaleFrame(frame, scale=0.5)
    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame1)
    cv.imshow('Video_resized1', frame2)
    
    if cv.waitKey(20) & 0xFF == ord('d'):       # 'd'를 누르면 종료
        break
    
capture.release()
cv.destroyAllWindows()
