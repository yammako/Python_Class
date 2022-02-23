# 파일 저장 및 열기
# DataFrame 객체를 excel, csv, txt등의 파일로 저장, 열기

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
df.index.name = '지원번호'
print(df)

# 파일 저장

# csv 파일로 저장 (데이터를 콤마로 구분하는 파일)
df.to_csv('Data_Visualization/pandas/score.csv', encoding='utf-8-sig')

# csv 파일로 저장 (데이터를 콤마로 구분하는 파일), 인덱스 제외
df.to_csv('Data_Visualization/pandas/score_no_index.csv', encoding='utf-8-sig', index=False)

# txt 파일로 저장 (항목을 탭으로 구분)
df.to_csv('Data_Visualization/pandas/score.txt', sep='\t')

# excel 파일로 저장
df.to_excel('Data_Visualization/pandas/score.xlsx')


# 파일 열기

# csv 파일 열기
df1 = pd.read_csv('Data_Visualization/pandas/score.csv')
print(df1)

df2 = pd.read_csv('Data_Visualization/pandas/score_no_index.csv')
print(df2)

# 제외하고 싶은 행을 설정하기
df3 = pd.read_csv('Data_Visualization/pandas/score_no_index.csv', skiprows=1)   # 1행 제외
print(df3)

# 제외하고 싶은 여러 행을 설정하기
df4 = pd.read_csv('Data_Visualization/pandas/score_no_index.csv', skiprows=[1,3,5])     # 1,3,5행 제외
print(df4)

# 지정된 행 수만큼만 가져오기
df5 = pd.read_csv('Data_Visualization/pandas/score_no_index.csv', nrows=4)     # 제목을 제외한 4개의 행만 가져옴
print(df5)

# 지정된 행 수만큼 그리고 지정된 행을 제외하고 가져오기
df6 = pd.read_csv('Data_Visualization/pandas/score_no_index.csv', skiprows=2, nrows=4)     # 2행 제외, 제목을 제외한 4개의 행만 가져옴
print(df6)

# 텍스트 파일 열기
df = pd.read_csv('Data_Visualization/pandas/score.txt', sep='\t')
print(df)

df = pd.read_csv('Data_Visualization/pandas/score.txt', sep='\t', index_col='지원번호')     # 인덱스 열을 지정하기
print(df)

# 엑셀 파일 열기
df = pd.read_excel('Data_Visualization/pandas/score.xlsx')
print(df)

df = pd.read_excel('Data_Visualization/pandas/score.xlsx', index_col='지원번호')        # 인덱스 열을 지정하기
print(df)