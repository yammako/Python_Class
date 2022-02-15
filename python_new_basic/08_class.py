# 반복되는 변수 & 메소드(함수)를 미리 정해놓은 틀 (설계도)
result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))

# 구조가 같은 함수, 변수등등의 틀을 미리 만들어 놓는 것
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(6))

# 일반적인 class 설계
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(1, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

# FourCal을 부모 class로 활용하여 자식 class 생성
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):                          # 부모 class에 있는 div 함수와 중복되는데 이때는 자식 class의 함수를 적용하게 됨. 이를 overriding이라 함.
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# b = FourCal(4,0)
# print(b.div())        # 0으로 나눌수 없으므로 에러 발생
c = SafeFourCal(4, 0)
print(c.div())          # 자식 class에서 0 예외처리를 했기 때문에 연산 가능

