# 조건문 if: if의 문장이 True 이면 다음 문장 실행, False이면 else 다음 문장 실행
# 조건문에서는 들여쓰기가 중요함. 들여쓰기가 같은 문장은 블럭으로 묶어 실행함.
# 조건식
# <: 작다
# >: 크다
# >=: 크거나 같다
# <=: 작거나 같다
# ==: 같다
# !=: 같지 않다
money = True
if money:
    print("Take a taxi")
else:
    print("Walk")

money = False
if money:
    print("Take a taxi")
else:
    print("Walk")

a = 1
b = 2
if a < b:
    print("Take a taxi")
else:
    print("Walk")

money = 2000
if money >= 3000:
    print("Take a taxi")
else:
    print("Walk")

money = 2000
card = 1
if money >= 3000 or card:
    print("Take a taxi")
else:
    print("Walk")

money = 2000
card = 1
if (money >= 3000) | card:
    print("Take a taxi")
else:
    print("Walk")

money = 2000
card = 1
if money >= 3000 and card:
    print("Take a taxi")
else:
    print("Walk")

money = 2000
card = True
if (money >= 3000) & card:
    print("Take a taxi")
else:
    print("Walk")

if 1 in [1,2,3]:
    print('Take a taxi')
else:
    print("Walk")

if 1 not in [1,2,3]:
    print('Take a taxi')
else:
    print("Walk")    

# 조건문을 만족할 때 아무 일도 하지 않으려면 pass 사용
if 1 in [1,2,3]:
    pass
else:
    print("Walk")

if 1 not in [1,2,3]:
    pass
else:
    print("Walk")

# 다중 조건문 elif
pocket = ['paper', 'cellphone']
card = False
a = True
if 'money' in pocket:
    print("Take a taxi")
elif card:
    print("Take a bus")
elif a:
    print("aa")
else:
    print("Walk")

# 조건문 간결형
# 일반적인 조건문
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

# 간결형
message = "success" if score >= 60 else "failure"
print(message)