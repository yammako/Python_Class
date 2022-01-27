# 숫자 자료형 
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# boolean 자료형 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 애완동물을 소개해 주세요~~
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 강아지 이름이 바뀌었을 때 위의 명령어를 다 고치는 것은 힘들기 때문에 변수 사용
animal = "강아지"   # 문자열
name = "연탄이"     # 문자열
age = 4             # 숫자
hobby = "산책"      # 문자열
is_adult = age >= 3 # boolean

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

animal = "고양이"   # 문자열
name = "해피"     # 문자열
age = 2             # 숫자
hobby = "낮잠"      # 문자열
is_adult = age >= 3 # boolean

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# str을 사용하지 않고 나이와 어른인지를 나타내고 싶을 경우에는 + 대신 ,를 사용하면 됨. ,는 한칸 띄우기가 포함되어 있음.
print("우리집 ", animal, "의 이름은 ", name, "에요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요? ", is_adult)

# 주석: 프로그램을 설명하지만 실행은 되지 않는 문장

#print("우리집 ", animal, "의 이름은 ", name, "에요")       한문장 주석처리는 #
'''
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요? ", is_adult)'''
'''여러문장을 한꺼번에 주석처리할 때는
따옴표 3개를 사용함.'''

# 아래의 3 문장을 한꺼번에 주석처리할 때는 블럭처리한 후 Ctrl + /를 하면 됨. 해제는 Ctrl + /를 다시 하면 됨.
# print("우리집 ", animal, "의 이름은 ", name, "에요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name, "는 어른일까요? ", is_adult)

# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : xx행 열차가 들어오고 있습니다.

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")