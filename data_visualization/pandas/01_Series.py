# Pandas : 파이썬에서 사용하는 데이터 분석 라이브러러
import pandas as pd
# Series: 1차원 데이터 형태
# 예) 1월부터 4월까지 평균 온도 데이터 (-20, -10, 10, 20)
temp = pd.Series([-20, -10, 10, 20])
print(temp)
print(temp[0])
print(temp[2])
# 인덱스 지정
temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
print(temp['Jan'])      # 인덱스가 숫자에서 내가 만든 월 이름으로 바뀌었다.
# print(temp['Jun'])    # 인덱스가 없으므로 에러 발생