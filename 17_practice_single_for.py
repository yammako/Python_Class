# 한줄로 for문 만들기
# 출석번호가 1, 2, 3, 4, 5가 있는데 출석번호 형식이 바뀌어서 100을 붙이기로 함 -> 101, 102, 103, 104, 105
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

출력문 예제
[O] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 50분)
[O] 3번째 손님 (소요시간: 5분)
...
[ ] 50번째 손님 (소요시간: 16분)

총 탑승 승객 : 2분
'''
from random import *
customer_no = range(1, 51)
total_customer_no = 0
for i in customer_no:
    driving_time = randint(5, 50)
    if 5 <= driving_time <= 15:
        print("[O] {0}번째 손님 (소요시간: {1}분)".format(i, driving_time))
        total_customer_no += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, driving_time))
print("총 탑승 승객 : {0}분".format(total_customer_no))