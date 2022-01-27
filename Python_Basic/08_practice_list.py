# 리스트
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
# 리스트를 사용하여 3 변수를 합침
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 칸에 탔다고 하면
subway.append("하하")
print(subway)

# 유재석과 조세호 사이에 정형돈을 넣고 싶다면
subway.insert(1, "정형돈")
print(subway)

# 뒤에서부터 한명씩 빼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모든 데이터 지우기
num_list.clear()
print(num_list)

# 리스트는 자료형에 구애를 받지 않는다
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 합치기
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)