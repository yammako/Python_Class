# 연산자
print(1+1)      # 2
print(3-2)      # 1
print(5*2)      # 10
print(6/3)      # 2
print(2**3)     # 2^3 = 8
print(5%3)      # 5 나누기 3의 나머지인 2 (나머지 구하는 연산자: %)
print(10%3)     # 1
print(5//3)     # 5를 3으로 나누었을 때 몫 1 (몫을 구하는 연산자: //)
print(10//3)    # 3
print(10 > 3)   # True
print(4 >= 7)   # False
print(10 < 3)   # False
print(3 == 3)   # True  (같다는 연산자: ==)
print(4 == 2)   # False
print(3 + 4 == 7)   # True
print(1 != 3)   # True (같지 않다는 연산자: !=)
print(not(1 != 3))  # False
print((3 > 0) and (3 < 5))  # True (동시 만족조건 연산자 and)
print((3 > 0) & (3 < 5))    # True (동시 만족조건 연산자 &)
print((3 > 0) or (3 > 5))   # True (둘 중 하나만 만족해도 되는 연산자 or)
print((3 > 0) | (3 > 5))   # True (둘 중 하나만 만족해도 되는 연산자 |)
print(5 > 4 > 3)            # True
print(5 > 4 > 7)            # False
print(2 + 3 * 4)            # 14
print((2 + 3) * 4)          # 20
number = 2 + 3 * 4          # 14
print(number)
number = number + 2         # 16
print(number)
number += 2                 # 18
print(number)
number *= 2                 # 36
print(number)
number /= 2                 # 18
print(number)
number -= 2                 # 16
print(number)
number %= 2                 # 0
print(number)