# 표준 입출력
print("Python", "Java")
print("Python" + "Java")
print("Python", "Java", sep = ",")  # 콤마 부분을 콤마로 출력
print("Python", "Java", sep = " vs ")  # 콤마 부분을 vs로 출력
print("Python", "Java", sep = " vs ", end = "?")  # 콤마 부분을 vs로 출력하고 ?가 있는 문자이 마지막이되어 한줄로 출력
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")    # ljust는 왼쪽 정렬이고 8은 8칸을 확보한다는 뜻, rjust는 오른쪽 정렬이고 4는 4칸을 확보한다는 뜻

# 은행 대기번호표
# 001, 002, 003, ...
for num in range(1, 21):
    # print("대기번호 : " + str(num))
    print("대기번호 : " + str(num).zfill(3))        # zfill(3)은 3자리 숫자에서 0을 채운다는 것

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")         # 문자열 형태로 입력이 됨
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

answer = 10
print(type(answer))
print("입력하신 값은 " + str(answer) + "입니다.")