# 지역변수는 함수에서만 사용하는 것
# 전역변수는 프로그램 전체에서 사용하는 것

gun = 10

def checkpoint(soldiers):   # 경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 수 : {0}".format(gun))       # 전역 변수 gun 출력
checkpoint(2)   # 2명이 경계 근무 나감      지역 변수 gun 출력
print("남은 총 : {0}".format(gun))          # 전역 변수 gun 출력

gun = 10

# 전역 변수 설정으로 함수 사용하는 법 (잘 사용하지 않음. 전역 변수가 많으면 프로그램에 혼돈이 생길 수 있음)
def checkpoint(soldiers):   # 경계근무
    global gun          # 전역 변수 설정
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

# 주로 사용하는 함수 (전역변수, 지역변수 사용하는 법)
def checkpoint_ret(gun, soldiers):   # 경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 수 : {0}".format(gun))       # 전역 변수 gun 출력
# checkpoint(2)   # 2명이 경계 근무 나감      지역 변수 gun 출력
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))          # 전역 변수 gun 출력

'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) X 키(m) X 22
여자 : 키(m) X 키(m) X 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender):
    if gender == "남자":
        weight = round((int(height)/100) * (int(height)/100) * 22, 2)
    else:
        weight = round((int(height)/100) * (int(height)/100) * 21, 2)
    return weight

height = input("키를 입력해 주세요 (cm): ")
gender = input("성별을 입력해 주세요 (남자/여자) : ")

weight = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))