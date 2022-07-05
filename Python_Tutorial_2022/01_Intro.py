# Python 소개
# 계산
print(2+3)  # 덧셈
print(3-2)  # 뺄셈
print(2*3)  # 곱셈
print(2/3)  # 나눗셈
print(2**3) # 지수승
print(2%3)  # 나머지 계산
print(3%2)  # 나머지 계산
print(6//4) # 몫 계산

# 데이터 할당
num = 10    # 10을 num 변수에 할당
print(num)
num += 2    # num에 2를 더해서 할당 (10+2) = 12
print(num)
num -= 2    # num에 2를 빼서 할당 (12-2) = 10
print(num)
num *= 2    # num에 2를 곱해서 할당 (10*2) = 20
print(num)
num /= 2    # num에 2를 나누어서 할당 (20/2) = 10
print(num)
num %= 6    # num에 6을 나누어 나머지를 할당 (10%6) = 4
print(num)
num **= 2   # num에 할당된 값에 2승을 한 값을 할당 (4**2) = 16
print(num)
num //= 7   # num을 7로 나눈 몫을 할당 (16//7) = 2
print(num)

# 논리 연산자

# 조건 연산자
num = 7
print(num > 7)      # False
print(num < 7)      # False
print(num >= 7)     # True
print(num <= 7)     # True
print(num != 7)     # False
print(num == 7)     # True

# AND 연산자
num = 7
print(num>=3 and num<=8)        # AND 연산은 두 조건을 모두 만족해야 참 (True), 만족하므로 True
print(num>=3 and num<=6)        # AND 연산은 두 조건을 모두 만족해야 참 (True), 만족하지 않으므로 False

# OR 연산자
num = 7
print(num>=3 or num<=8)        # OR 연산은 두 조건 중 하나만 만족해도 참 (True), 만족하므로 True
print(num>=3 or num<=6)        # OR 연산은 두 조건 중 하나만 만족해도 참 (True), 만족하므로 True

# NOT 연산자
num = 7
print(not(num>=3))        # NOT 연산은 True는 False로 False는 True로 변환, True의 NOT이므로 False