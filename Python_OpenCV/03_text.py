# OpenCV 글꼴 종류
# cv.FONT_HERSHEY_SIMPLEX: 보통크기의 세리프 (serif) 글꼴
# cv.FONT_HERSHEY_PLAIN: 작은 크기의 세리프 글꼴
# cv.FONT_HERSHEY_SCRIPT_SIMPLEX: 필기체 글꼴
# cv.FONT_HERSHEY_TRIPLEX: 보통 크기의 세리프 글꼴
# cv.FONT_ITALIC: 기울임체

import cv2 as cv
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR = (255,255,255)   # 색깔
THICKNESS = 3           # 두께
SCALE = 2               # 크기

# 이미지, 문자열, 시작위치, 폰트, 크기, 색깔, 두께, 선 타입
cv.putText(img, "Hello Simplex", (20,50), cv.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS, cv.LINE_AA)
cv.putText(img, "Hello Plain", (20,150), cv.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS, cv.LINE_AA)
cv.putText(img, "Hello Script Simplex", (20,250), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS, cv.LINE_AA)
cv.putText(img, "Hello Triplex", (20,350), cv.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS, cv.LINE_AA)
cv.putText(img, "Hello Italic", (20,450), cv.FONT_HERSHEY_TRIPLEX | cv.FONT_ITALIC, SCALE, COLOR, THICKNESS, cv.LINE_AA)
cv.imshow('Text', img)

# 한글
from PIL import ImageFont, ImageDraw, Image

def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR = (255,255,255)   # 색깔
FONT_SIZE = 30

# 이미지, 문자열, 시작위치, 폰트, 크기, 색깔, 두께, 선 타입
img = myPutText(img, "한글 텍스트", (20,50), FONT_SIZE, COLOR)
cv.imshow("Korean text", img)

cv.waitKey(0)
cv.destroyAllWindows()