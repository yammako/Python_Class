# 이미지 저장
import cv2 as cv
img = cv.imread('openCV/glass.jpg', cv.IMREAD_GRAYSCALE)  # 흑백으로 이미지 불러오기
cv.imshow('Gray', img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("openCV/glass_gray.jpg", img)    # 이미지 저장

# 동영상 저장
video = cv.VideoCapture('openCV/Piano.mp4')

# 코덱 정의
# fourcc = cv.VideoWriter_fourcc('D', 'I', 'V', 'X')
fourcc = cv.VideoWriter_fourcc(*'DIVX')     # 위의 코덱 DIVX를 따로 적는 것이 귀찮으므로 *을 추가하여 DIVX를 바로 씀.
width = round(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv.CAP_PROP_FPS)
fps1 = fps * 2
out = cv.VideoWriter('openCV/output_piano.avi', fourcc, fps, (width, height))
out_fast = cv.VideoWriter('openCV/output_piano_fast.avi', fourcc, fps1, (width, height))


while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    out.write(frame)    # 영상 저장 (소리는 저장되지 않음)
    out_fast.write(frame)    # 영상 저장 (소리는 저장되지 않음)
    cv.imshow('Video', frame)
    if cv.waitKey(1) == ord('q'):
        break

out.release()
out_fast.release()
video.release()
cv.destroyAllWindows()
