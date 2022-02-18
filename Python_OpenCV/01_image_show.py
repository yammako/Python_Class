# OpenCV를 사용한 이미지 입력과 출력
import cv2 as cv        # openCV 라이브러리를 불러옴
img = cv.imread('openCV/glass.jpg')     # glass.jpg 파일을 읽어옴 -> cv.imread('파일경로/파일명') 함수 사용

gray = cv.imread('openCV/glass.jpg', cv.IMREAD_GRAYSCALE)     # glass.jpg 파일을 흑백이미지로 읽어옴
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    # 컬러 이미지를 흑백 이미지로 변환

cv.imshow('Glass', img)             # 이미지 출력 -> cv.imshow('창이름', 영상변수) 함수 사용
cv.imshow('Gray', gray)

# cv.waitKey(0)           # 키가 입력될 때까지 기다림 -> (숫자)ms 동안 기다림.

# 동영상 파일 출력
video = cv.VideoCapture('openCV/Piano.mp4')
while video.isOpened():
    ret, frame = video.read()       # ret: 성공 여부, frame: 받아온 프레임
    if not ret:
        print("더 이상 가져올 프레임이 없어요.")
        break

    cv.imshow('Video', frame)

    if cv.waitKey(25) == ord('q'):              # waitKey(숫자): 숫자 값에 의해 동영상 속도 조절
        print("사용자 입력에 의해 종료합니다.")
        break

video.release()     # 비디오 자원 해제
cv.destroyAllWindows()      # 모든 윈도우 닫음.

# 카메라 출력
cap = cv.VideoCapture(0)
if not cap.isOpened():
    exit()

while True:
    ret, frame = cap.read()       # ret: 성공 여부, frame: 받아온 프레임
    if not ret:
        break

    cv.imshow('Camera', frame)

    if cv.waitKey(1) == ord('q'):              # waitKey(숫자): 숫자 값에 의해 동영상 속도 조절
        print("사용자 입력에 의해 종료합니다.")
        break

cap.release()

cv.destroyAllWindows()      # 모든 윈도우 닫음.


