# 내장 함수 (기본 함수)

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요? ")
# print("{0}는 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())
# print(dir(random))

lst = [1, 2, 3]
print(dir(lst))         # lst에서 사용할 수 있는 것들 표시

name = "Jim"
print(dir(name))        # name에서 사용할 수 있는 것들 표시

# 구글에서 list of python builtin으로 검색하면 내장 함수를 볼 수 있다.