# 도형 그리기
# 빈 스케치북 만들기
import cv2 as cv
import numpy as np

# 세로 480 x 가로 640, 3 채널 (BGR) 스케치북 만들기
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
cv.imshow("Black Sketchbook", img)
img[:] = (255,0,0)          # Blue 스케치북
cv.imshow("Blue Sketchbook", img)
img[:] = (0,255,0)          # Green 스케치북
cv.imshow("Green Sketchbook", img)
img[:] = (0,0,255)          # Red 스케치북
cv.imshow("Red Sketchbook", img)
img[:] = (255,255,255)      # White 스케치북
cv.imshow("White Sketchbook", img)

# 일부 영역 색칠
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
img[100:200, 200:300] = (255,255,255)           # 세로 100:200, 가로:200:300 영역 하얀색으로 색칠
cv.imshow("Filled white in the partial area", img)

# 직선
# 직선의 종류 
# cv.LINE_4                 # 상하좌우 방향으로만 선을 그을 수 있다. 선의 화질이 가장 떨어짐.
# cv.LINE_8 (Default)       # 한점에서 8방향으로 선을 그을 수 있다. 즉, 대각선을 그릴 수 있다. 선의 화질이 향상됨.
# cv.LINE_AA                # 가장 선명한 선을 그을 수 있다.
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
COLOR = (0, 255, 255)       # Yellow
THICKNESS = 3               # 두께
cv.line(img, (50,100), (400,50), COLOR, THICKNESS, cv.LINE_8)   # img 이미지에 (50,100) 시작점에서 (400,50) 끝점까지 COLOR, THICKNESS를 가지는 직선을 그린다.
cv.line(img, (50,200), (400,150), COLOR, THICKNESS, cv.LINE_4)   # img 이미지에 (50,200) 시작점에서 (400,150) 끝점까지 COLOR, THICKNESS를 가지는 직선을 그린다.
cv.line(img, (50,300), (400,250), COLOR, THICKNESS, cv.LINE_AA)   # img 이미지에 (50,300) 시작점에서 (400,250) 끝점까지 COLOR, THICKNESS를 가지는 직선을 그린다.
cv.imshow("Line", img)

# 원
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
COLOR = (255, 255, 0)       # 옥색
RADIUS = 50                 # 반지름
THICKNESS = 10               # 두께
cv.circle(img, (200,100), RADIUS, COLOR, THICKNESS, cv.LINE_AA)     # 원 중심, 반지름, 색깔, 두께, 라인 타입을 입력하여 원을 그린다.
cv.circle(img, (400,100), RADIUS, COLOR, -1, cv.LINE_AA)            # 원 내부를 색으로 채우기
cv.circle(img, (400,100), RADIUS, COLOR, cv.FILLED, cv.LINE_AA)    # 원 내부를 색으로 채우기 다른 표현 cv.FILLED 사용
cv.imshow('Circle', img)

# 사각형
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
COLOR = (0, 255, 0)       # 녹색
THICKNESS = 3               # 두께
cv.rectangle(img, (100,100), (200,200), COLOR, THICKNESS, cv.LINE_AA)   # 시작점부터 끝점까지 색깔, 두께, 라인 타입을 가지는 사각형을 그린다.
cv.rectangle(img, (300,100), (400,300), COLOR, -1, cv.LINE_AA)      # 사각형 내부를 색깔로 채운다.
cv.imshow('Rectangle', img)

# 다각형
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
COLOR = (0, 0, 255)       # 빨간색
THICKNESS = 3               # 두께
pts1 = np.array([[100,100],[200,100],[100,200]])
pts2 = np.array([[400,100],[500,100],[400,200]])
cv.polylines(img, [pts1], True, COLOR, THICKNESS, cv.LINE_AA)           # 선을 연결할 점들의 위치, 도형의 닫힘 여부, 색깔, 두께, 선 타입
cv.polylines(img, [pts2], False, COLOR, THICKNESS, cv.LINE_AA)
cv.imshow('Polylines', img)
img = np.zeros((480,640,3), dtype=np.uint8)     # Unsigned integer 8bit black
cv.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv.LINE_AA)
cv.imshow('Polylines1', img)
pts3 = np.array([[[100,300],[200,300],[100,400]], [[200,300],[300,300],[300,400]]]) # 2개의 삼각형 점 위치 지정
cv.fillPoly(img, pts3, COLOR, cv.LINE_AA)
cv.imshow('Filled Polylines', img)
cv.waitKey(0)
cv.destroyAllWindows()
