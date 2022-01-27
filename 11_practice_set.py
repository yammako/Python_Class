# 세트 (집합)
# 중복 불가, 순서 없음
my_set = {1,2,3,3,3}    # 세트는 {}로 만듦, 사전과 달리 키가 없음
print(my_set)       # 중복 불가라서 3은 하나만 출력

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 만들기
print(java & python)
print(java.intersection(python))

# 합집합 만들기
print(java | python)
print(java.union(python))

# 차집합 만들기 (java 할 수 있지만 python 못하는 사람)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 할 줄 모르게 되면
java.remove("김태호")
print(java)