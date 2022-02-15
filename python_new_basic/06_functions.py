# 함수는 입력과 출력, 처리문장으로 이루어져 있음.
# def 를 사용하여 함수 생성
from re import A, I


def sum(a, b):
    result = a + b
    return result

print(sum(1,2))

# 입력값이 없는 함수
def say():
    return 'Hi'

print(say())

# return이 없는 함수
def sumPrint(a, b):
    print("%d + %d = %d입니다." % (a, b, a+b))

sumPrint(1,2)

# 입력, return 없는 함수
def say():
    print("Hi")

say()

# 입력 변수의 개수를 정할 수 없을 경우 *변수명을 사용. 주로 *args를 사용
def sumMany(*args):
    sum = 0
    for i in args:
        sum += I
    return sum

print(sumMany(1,2,3,4))
print(sumMany(1,2,3,4,5))

# dictionary와 같이 키와 값을 갖는 입력변수를 사용할 경우 **변수명을 사용
def printKeyword(**kwargs):
    for k in kwargs.keys():
        if k == "name":
            print("당신의 이름은 :", kwargs[k])
        elif k == "lang":
            print("당신이 사용하는 언어는 :", kwargs[k])
        elif k == "hobby":
            print("댱신의 취미는 :", kwargs[k])
        else:
            pass

printKeyword(name="Cho", lang = "Python", hobby = "Programming")

# 여러 개의 값을 return하는 경우는 tuple 형태로 리턴됨
def sum_and_mul(a, b):
    return a+b, a*b

print(sum_and_mul(1,2))     # tuple 형태로 모두 출력
print(sum_and_mul(1,2)[0])  # 덧셈 결과만 출력
print(sum_and_mul(1,2)[1])  # 곱셈 결과만 출력

# 입력 변수 초기값 미리 설정하기
def sayMyself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

sayMyself("Cho", 18)
sayMyself("Cho", 18, False)
sayMyself(old = 19, name = "Cho", man = False)

# Local, Global 변수
a = 1           # Global 변수
def vartest(a):
    a = a + 1   # Local 변수
    print("Local a = ", a)
    return a

vartest(a)
print("Global a = ", a)

b = vartest(a)
print("b = ", b)

# 함수 축약형
def add(a,b):
    return a+b

print(add(1,2))

add1 = lambda a, b: a+b
print(add1(1,2))

# 함수를 리스트로 표현하기
myFuncList = [lambda a, b: a+b, lambda a, b: a*b]
print(myFuncList[0](1,2))
print(myFuncList[1](1,2))

# 내장함수
# input: String을 입력으로 받음.
a = input("숫자를 입력하세요: ")
print("입력하신 숫자는 %s입니다." % a)

a = input("숫자를 입력하세요: ")
b = input("숫자를 입력하세요: ")
print("%s + %s = %d 입니다." % (a,b,int(a)+int(b)))

# print
for i in range(10):
    print(i, end=" ")       # 출력 후 마지막에 줄바꿈이 아닌 공백 출력

for i in range(10):
    print(i, end="Hi")       # 출력 후 마지막에 줄바꿈이 아닌 Hi 출력


