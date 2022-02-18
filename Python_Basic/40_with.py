# with는 객체를 변수로 처리해 준다.
with open("Python_Basic/score.txt", encoding="UTF8") as f:
    for line in f:
        print(line, end="")