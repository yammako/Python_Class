# DataFrame 생성: 2차원 데이터
# 예) 슬램덩크 주요 인물 8명에 대한 데이터 (사전 자료 구조 : dictionary)
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
print(data)
print(type(data))
print(data['이름'])
print(data['키'])

# DataFrame 생성하기
import pandas as pd
df = pd.DataFrame(data)
print(df)
# 데이터 접근
print(df['이름'])
print(df['키'])
print(df[['이름', '키']])       # 2개 이상의 열을 불러오고 싶으면 []를 두면 사용

# DataFrame 생성에서 인덱스 지정하기
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
print(df)

# DataFrame 생성에서 일부 열만 가져오기 (Column 지정)
df = pd.DataFrame(data, columns=['이름', '학교', '키'])
print(df)
df = pd.DataFrame(data, columns=['이름', '키', '학교'])
print(df)