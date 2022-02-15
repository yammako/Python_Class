# 숫자형 (Numerical)

# 정수형 (Integer)
a = 1
print("a = ", a, ". Type of a is ", type(a))

# 실수 (Float)
a = 1.
print("a = ", a, ". Type of a is ", type(a))
b = 4e10
print("b = ", b, ". Type of b is ", type(b))

# 2진수, 8진수, 16진수
a = 0b11        # 2진수 11 -> 10진수로 3
b = 0o37        # 8진수 37 -> 10진수로 31
c = 0xFF        # 16진수 FF -> 10진수로 255
print("a = ", a, "b = ", b, 'c = ', c)

# 사칙연산
a = 3
b = 5
print("a + b = ", a+b)
print("a - b = ", a-b)
print("a x b = ", a*b)
print("a / b = ", a/b)

# 나눗셈의 몫과 나머지
print("a / b 의 몫 ", a//b)
print("a / b 의 나머지 ", a%b)



# 문자열 (String)
s = "Hello World"
print("s = ", s, ". Type of s is ", type(s))

# 따옴표를 문자열에 추가하기 \' 사용
s = "\'Python\' is my favorite language"
print("s = ", s, ". Type of s is ", type(s))

# 여러줄로 이루어진 문자열 만들기
s = '''It has three sentences.
Python is my favorite language.
C is my second language.
'''
print("s = ", s, ". Type of s is ", type(s))

# 인덱싱 (indexing): Python에서 0부터 시작해서 인덱싱을 한다. (좌에서 우)
print("s[0] = ", s[0])
print("s[0:8] = ", s[:8])   # 좌에서 8개의 문자 출력
print("s[8:end] = ", s[8:])   # 우에서 8개의 문자 출력

# 슬라이싱 a[이상:미만:간격] -> a[1:8:2] -> 2번째요소부터 8번째요소까지 2칸 간격으로 인덱싱
# a[::2] -> 처음부터 끝까지 두칸간격
# a[1::2] -> 두번째부터 끝까지 두칸간격
# a[:8:3] -> 처음부터 8번째요소까지 3칸간격
b = '12345678'
print("두칸씩 띄워서 문자 출력: ", b[::2])
b = '1 2 3 4 5 6 7 8'
print("두칸씩 띄워서 문자 출력: ", b[::2])
print("3번째 문자부터 두칸씩 띄워서 문자 출력: ", b[2::2])
print("3번째 문자부터 8번째 문자까지 두칸씩 띄워서 문자 출력: ", b[2:8:2])

# 음수는 반대방향으로 인덱싱한다. (우에서 좌)
print("우측에서 두칸씩 띄워서 문자 출력: ", b[-1::-2])
print("우측 3번째 문자부터 두칸씩 띄워서 문자 출력: ", b[-3::-2])
print("우측 5번째 문자부터 11번째 문자까지 두칸씩 띄워서 문자 출력: ", b[-5:-11:-2])

# 문자열 포맷
# %d -> 정수 리턴, %s -> 문자 리턴, %f -> 실수 리턴, %2.3f -> 정수 2자리, 소숫점 3자리 실수 리턴, %.3f -> 정수는 그대로, 소수점 3자리까지
number = 10
day = "three"
weight = 87.12345
a = "I ate %d apples. So I was sick for %s days. Therefore, my weight is %2.3f" % (number, day, weight)
b = "I ate %d apples. So I was sick for %s days. Therefore, my weight is %.3f" % (number, day, weight)
print(a)
print(b)

# 문자열 개수
a = "hobby"
print(a.count('b'))

# 문자의 위치 인덱스 찾기
print(a.find('o'))
print(a.find('b'))

# join
a = ",".join("abcd")    # 콤마를 기준으로 문자를 쪼갠다.
print(a)
a = ",".join(["ab", "cd", "ef"])    # 콤마를 기준으로 문자를 쪼갠다.
print(a)

# 대소문자 변환
a = "hi"
print(a.upper())
b = "HELLO"
print(b.lower())

# 문자열 공백없애기 strip
a = "     HI,       "
b = "I am a boy."
print(a,b)
print(a.strip(), b)

# 문자열 바꾸기
a = "I am a boy."
print(a.replace("boy", "girl"))

# 문자열을 공백을 기준으로 나누어서 리스트 생성
b = a.split()
print(b[0])
print(b[1])
print(b)


# List []
a = [1,2,"int", "Kim", ["Cho", "Python"]]
print(a)
print(a[0])
print(a[3])
print(a[4])
print(a[4][0])
print(a[:4])

# List 더하기
a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
print(c)

# List 곱하기
print(a * 3)    # a라는 리스트를 3번 합쳐서 출력

# List 값 수정
a = ["Python", "Java", "C++"]
print(a)
a[0] = "C#"
print(a)
a[:3]=["Fotran", "Cobol", "Basic"]
print(a)
a[:2]=[]
print(a)
a = ["Python", "Java", "C++"]
print(a)
del a[0]
print(a)

# List 추가
a = ["Python", "Java", "C++"]
a.append('Fotran')
print(a)

# List 정렬
a.sort()
print(a)

# List 뒤집기
a.reverse()
print(a)

# List 요소 인덱스 출력
print(a.index("Python"))

# 특정 인덱스에 List 요소 삽입하기
a.insert(3, "C#")
print(a)

# 특정 요소를 List에서 삭제하기
a.remove("Java")
print(a)
a = ["Python", "Java", "C++", "Java", "Java"]
a.remove("Java")        # 첫번째 Java만 삭제됨.
print(a)

# List의 마지막 요소를 빼내기, List에서 없어짐.
print(a.pop())
print(a)

# List에서 특정 요소의 개수
a = ["Python", "Java", "C++", "Java", "Java"]
print(a.count("Java"))
a.pop()
print(a.count("Java"))

# List 확장
print(a)
a.extend(["MATLAB", "Javascript"])
print(a)



# Tuple () -> 변경불가능
t1 = (1,2,'a','b')
# del t1[0]         에러 발생 변경불가능
# 보는 것은 가능
print(t1[:2])
t2 = (3,4)
print(t1+t2)
t1 = t1 * 3
print(t1)


# Dictionary {} -> {key:data, key:data}
dic = {'name':'pey', 'age':15}
print(dic['name'])
dic['job'] = 'programmer'
print(dic)
dic['name'] = 'Eric'
print(dic)

# key만 따로 출력
print(dic.keys())
for k in dic.keys():
    print(k)

# value만 따로 출력
print(dic.values())
for v in dic.values():
    print(v)

# item으로 출력
print(dic.items())
for k,v in dic.items():
    print('키는 :', k)
    print('밸류는 :', v)

# get 명령을 사용하면 key가 없을 때 에러가 아닌 None을 출력
print(dic.get(4))

# dictionary에 key가 있는지 없는지 확인하는 법
print(4 in dic)
print('name' in dic)



# 집합 set -> 중복을 허용하지 않는다. 순서가 없다.
# 집합을 표현하는 두가지 방법
s1 = set([1,2,3])   # 첫번째 방법
s1 = {1,2,3}        # 두번째 방법
print(s1)

# 집합 사용 예 -> 리스트에서 중복되는 값을 제거한 후 리스트로 재설정하고 싶을 때
l = [1,2,2,3,3]
newList = list(set(l))
print(l)
print(newList)

# 교집합
s1 = set([1,2,3,4,5,6])
s2 = {4,5,6,7,8,9}
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)

# 집합에 추가하기
s1.add(7)
print(s1)
s1.update([7,8,9,1])
print(s1)

# 집합에서 제거하기
s1.remove(1)
print(s1)


# 불리언 (Boolean): 논리값 True, False
# 문자열이 있으면 True, 없으면 False
# 리스트, 딕셔너리, 튜플 요소가 있으면 True, 없으면 False
# 1은 True, 0은 False
# None은 False
a = True
print(a)
print(type(a))

a = "Hello"
if a:
    print(a)

a = ""
if a:
    print(a)
else:
    print("No string")

a = [1,2,3,4,5]
while a:
    print(a)
    a.pop()

# 변수 Variable: 데이터를 저장하는 공간
a = 1
b = "Python"
c = True

a = [1,2,3]
b = a
a[1] = 4
print(a)
print(b)        # b를 변화시키지 않았지만 a와 b는 같은 변수 주소를 가지므로 값이 변함

# 변수의 주소 출력
print(id(a))
print(id(b))

# a변수의 주소가 아닌 값을 복사하고 싶을 때
b = a[:]
a[1] = 2
print(a)
print(b)
print(id(a))
print(id(b))    # b의 주소가 바뀌었다.

# 변수를 복사하는 또 다른 방법
from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4
print(a)
print(b)

# 변수 할당
a, b = ('python', 'life')
print(a)
print(b)

(a, b) = 'python', 'life'
print(a)
print(b)

[a, b] = ['python', 'life']
print(a)
print(b)

a = b = 'hello'
print(a)
print(b)

# 변수 스와핑
# 일반적인 언어에서 사용하는 스와핑
a = 3
b = 5
tmp = b
b = a
a = tmp
print(a)
print(b)

# Python에서 사용하는 스와핑
a, b = b, a
print(a)
print(b)
