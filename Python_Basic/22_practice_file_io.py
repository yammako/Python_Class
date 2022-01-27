# 파일 입출력
# 파일 쓰기
score_file = open("score.txt", "w", encoding="utf8")    # 파일 만드는 명령 open, w는 쓰기, utf8은 한글 사용을 위해 사용
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")    # 기존 파일에 내용 추가할 경우 a 옵션 사용
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일 읽기
score_file = open("score.txt", "r", encoding="utf8")    # 파일을 읽을 때는 r 옵션 사용
print(score_file.read())        # .read()는 파일의 내용을 불러옴
score_file.close()

# 파일 내용을 한줄씩 불러오기
score_file = open("score.txt", "r", encoding="utf8")    # 파일을 읽을 때는 r 옵션 사용
print(score_file.readline())    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
print(score_file.readline())    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
print(score_file.readline())    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
print(score_file.readline())    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
score_file.close()

# 줄바꿈을 하기 싫을 때
score_file = open("score.txt", "r", encoding="utf8")    # 파일을 읽을 때는 r 옵션 사용
print(score_file.readline(), end="")    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
print(score_file.readline(), end="")    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
print(score_file.readline(), end="")    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
print(score_file.readline(), end="")    # 한 줄씩 읽어오고 커서는 다음 줄로 이동
score_file.close()

# 몇 줄인지 모를 때
score_file = open("score.txt", "r", encoding="utf8")    # 파일을 읽을 때는 r 옵션 사용
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 리스트에 넣어 사용하는 법
score_file = open("score.txt", "r", encoding="utf8")    # 파일을 읽을 때는 r 옵션 사용
lines = score_file.readlines()  # readlines는 list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()