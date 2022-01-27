# 입력 파라미터가 없는 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 입력 파라미터가 있는 경우
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    if balance >= money + commission:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - (money + commission)))
        return balance - (money + commission)
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
balance = withdraw_night(balance, 500)
balance = withdraw(balance, 2000)
print(balance)

# 함수의 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 만약 나이가 같다면 나이를 입력할 필요가 없다. 이 때 기본값을 사용한다.
def profile1(name, main_lang, age=17):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile1("유재석", "파이썬")
profile1("김태호", "자바")

# 키워드를 사용한 함수 파라미터 입력
profile1(main_lang="자바", name="유재석")
profile1(age = 18, name="김태호", main_lang="파이썬")

# 가변인자를 이용한 함수 호출
def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile2("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile3(name, age, *language):    # 가변인자는 *을 사용한다. 
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")        # 줄바꿈을 피하기 위해 end=" "를 사용
    for lang in language:   
        print(lang, end=" ")        # 줄바꿈을 피하기 위해 end=" "를 사용
    print()     # 줄바꿈을 위해 print()를 사용

profile3("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile3("김태호", 25, "Kotlin", "Swift")
