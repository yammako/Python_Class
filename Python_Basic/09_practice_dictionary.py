# 사전 dictionary {}를 사용함. 키와 데이터로 구성
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# print(cabinet[5])     5라는 키가 없으므로 에러 발생
print(cabinet.get(5))   # 키가 없을 경우 None을 리턴
print("hi")

print(cabinet.get(5, "사용 가능"))  # 키가 없을 경우 None이 아니라 "사용 가능"이란 글자를 리턴하고 싶을 경우
print("hi")

print(3 in cabinet)     # 키가 있는지 확인 : 있으면 True, 없으면 False 리턴
print(5 in cabinet)     # 키가 있는지 확인 : 있으면 True, 없으면 False 리턴

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님 : 키 삭제
del cabinet["A-3"]
print(cabinet)

# 키만 출력
print(cabinet.keys())

# 데이터값만 출력
print(cabinet.values())

# 키, 데이터를 쌍으로 출력
print(cabinet.items())

# dictionary 모두 지우기
cabinet.clear()
print(cabinet)