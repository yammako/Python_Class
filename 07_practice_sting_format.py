print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)  # %d에 20을 대입함. d는 정수를 의미
print("나는 %s을 좋아해요." % "파이썬")     # %s는 문자열
print("Apple은 %c로 시작해요." % "A")       # %c는 단일문자
print("나는 %s 살입니다." % 20)         # 숫자는 문자열로도 표현가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))        # 여러 값을 출력할 때

# 방법 2
print("나는 {}살입니다.".format(20))    # format 괄호 속의 데이터를 {}에 리턴
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))    # {}속에 숫자가 없으면 데이터를 순차적으로 리턴
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  # {}속에 숫자가 있으면 숫자 순서대로 데이터를 리턴
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))     # 변수를 리턴
# 변수를 미리 설정하고 출력할 경우
age = 16
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")     # 변수를 리턴

# \n 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# 저는 "코딩"입니다. 를 출력하고 싶을 때
print('저는 "코딩"입니다.')
print("저는 \"코딩\"입니다.")
print("저는 \'코딩\'입니다.")

# \\ 문장 내에서 \
print("C:\\Users\\Coding")

# \r 커서를 맨 앞으로 이동
print("Red Apple\rPine")    # Red Apple을 출력한 후 커서가 앞으로 가서 Pine을 다시 출력하기 때문에 PineApple이 출력됨.

# \b 백스페이스 (한 글자 삭제)
print("Redd\bApple")    # \b 앞의 d를 삭제

# \t 탭
print("Red\tApple")

'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                (nav)                 (5)            (1)            (!)
예) 생성된 비밀번호 : nav51!
'''

sentence = "http://naver.com"
# sentence = "http://daum.net"
sentence1 = sentence.replace("http://", "")     # 규칙 1
print(sentence1)
sentence1 = sentence1[:sentence1.index(".")]    # 규칙 2
print(sentence1)
password = sentence1[:3] + str(len(sentence1)) + str(sentence1.count('e')) + "!"    # 규칙 3
print(sentence1[:3])
print(str(len(sentence1)))
print(sentence1.count('e'))
print("!")
# 최종 출력
print("{0}의 비밀번호는 {1} 입니다.".format(sentence, password))