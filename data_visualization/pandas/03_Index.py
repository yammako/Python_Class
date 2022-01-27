# 인덱스 : 데이터에 접근할 수 있는 주소값
lst = ['유재석', '하하']
print(lst[0])
print(lst[1])

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

import pandas as pd
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
print(df)
print(df.index)     # 인덱스 값 출력

# 인덱스 이름 설정
df.index.name = '지원번호'
print(df)

# 인덱스 초기화
print(df.reset_index())     # 실제 데이터에 인덱스 초기화 반영 안됨
print(df)
print(df.reset_index(drop=True, inplace=True))     # 실제 데이터에 인덱스 초기화 반영
print(df)

# 인덱스 설정
print(df.set_index('이름'))
print(df)
# 실제 데이터에 반영하려면
print(df.set_index('이름', inplace=True))
print(df)

# 인덱스 정렬
print(df.sort_index())      # 오름차순으로 정렬
print(df)
print(df.sort_index(ascending=False))      # 오름차순으로 정렬
print(df)
# 실제 데이터에 반영하려면
print(df.sort_index(ascending=False, inplace=True))      # 오름차순으로 정렬
print(df)