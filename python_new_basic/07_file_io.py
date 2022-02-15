# 파일 읽고 쓰기
# r: 읽기모드, w: 쓰기모드, a: 추가모드
# 쓰기 모드
f = open("New.txt", 'w', encoding="UTF-8")      # UTF-8을 사용하면 한글입력 가능
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 읽기 모드 (한줄읽기)
f = open("New.txt", 'r', encoding="UTF-8")
line = f.readline()         # 한줄씩 입력
print(line)
f.close()

# 파일 내용 모두 읽기
f = open("New.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# readlines 사용하기 (List 형태로 불러오기 때문에 for문을 사용하여 출력함)
f = open("New.txt", 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines:
    #print(line, end="")
    #print(line.strip("\n"))
    print(line.strip("\n"), end=" ")
f.close()

# read 사용하기 (통째로 불러오기)
f = open("New.txt", 'r', encoding="UTF-8")
lines = f.read()
print(lines)
f.close()

# 추가 모드: 쓰기 모드는 파일 내용을 덮어쓰는 것이고 추가 모드는 파일 내용에 새로운 내용을 추가하는 것
f = open("New.txt", 'a', encoding="UTF-8")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

f = open("New.txt", 'r', encoding="UTF-8")
lines = f.read()
print(lines)
f.close()

# with문 사용하기, f.close() 필요없음.
with open("New.tixt", "w") as f:
    f.write("Life is too short, you need Python")
