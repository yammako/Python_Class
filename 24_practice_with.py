# with 
import pickle
# with는 file close가 필요 없다.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# with를 사용해서 파일 쓰기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
# with를 사용해서 파일 읽기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.
'''

for week in range(1, 51):
    with open("{0}주차.txt".format(week), "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :".format(week))