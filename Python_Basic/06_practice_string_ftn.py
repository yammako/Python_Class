python = "Python is Amazing"
print(python.lower())   # 모든 문자열을 소문자로 변환
print(python.upper())   # 모든 문자열을 대문자로 변환
print(python[0].isupper())  # 문자열의 첫문자가 대문자인지 알아보는 것
print(len(python))      # 문자열의 길이 구하기
print(python.replace("Python", "Java"))     # 문자열에서 바꾸고 싶은 문자열을 찾아서 다른 문자열로 바꾸기

index = python.index("n")       # 문자열에서 n이 처음 나오는 위치 찾기
print(index)
index = python.index("n", index + 1)    # 문자열에서 n이 두번째로 나오는 위치 찾기
print(index)
print(python.find("Java"))      # 문자열에서 찾는 문자열이 없으면 -1을 리턴
# print(python.index("Java"))      # 문자열에서 찾는 문자열이 없으면 에러가 남
print(python.count("n"))        # 문자열에서 n이 몇 번 있는지 구함