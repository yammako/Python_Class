import cv2 as cv                        # OpenCV 패키지 사용, cv2를 cv로 사용, OpenCV 패키지 내의 함수를 사용할 때 cv.을 먼저 쓰고 함수명을 써야 함.

# Read Image
img = cv.imread('openCV/Koala.jpg')    # imread: 영상 입력하는 함수 (파일 경로 설정해야 함.)
img1 = cv.imread('openCV/large_dark_cave.jpg') # 아주 큰 해상도를 가지는 영상 입력
cv.imshow('Koala', img)                 # imshow: 영상 출력하는 함수, ('윈도우명', 영상 변수)를 입력해야 함.
cv.imshow('Large Image', img1)          # 모니터 해상도보다 커서 윈도우가 화면보다 더 큼.
cv.waitKey(0)                           # 어떠한 키 값을 받을 때까지 윈도우 종료하지 않음.

# Read Video
# capture = cv.VideoCapture(0)            # 카메라를 사용항 동영상 출력
# capture = cv.VideoCapture(1)            # 카메라를 사용항 동영상 출력
capture = cv.VideoCapture('openCV/Piano.mp4')  # 동영상 파일 출력

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()


