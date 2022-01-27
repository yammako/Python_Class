# 튜플 (내용 추가나 변경 불가, 대신 리스트 보다 속도가 빠름)
menu = ("돈까스", "치즈까스")   # ()를 사용하여 튜플 생성
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
name, age, hobby = ("김종국", 20, "코딩")
print(name, age, hobby)