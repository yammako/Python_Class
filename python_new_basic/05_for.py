# For문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    else:
        print("%d번 학생은 합격입니다." % number)

sum = 0
for i in range(1, 11):      # 1 ~ 10까지 순서대로 처리
    print(i)
    sum += i
print(sum)

# 2중 for문
for i in range(2,10):
    for j in range(1,10):
        print("%d x %d = %d" % (i, j, i*j))

# for문을 사용하여 list 만들기
a = [1,2,3,4]
result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)

print(result)

# 간략하게 표현
result = [num * 3 for num in a if num % 2 == 0]
print(result)


# 다른 예제
result = []
for x in range(2,10):
    for y in range(1,10):
        result.append(x * y)

print(result)
# 간략한 표현
result = [x * y for x in range(2,10) for y in range(1, 10)]
print(result)