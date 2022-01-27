# 구글에서 list of python modules 하고 검색하면 외부 함수를 볼 수 있다.
# glob : 경로 내의 폴더 / 파일 목록 조회 (도스에서는 dir과 같은 기능)
import glob
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 디렉토리 표시

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())     # glob과 같은 기능

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)   # 100일 저장
print("우리가 만난지 100일은 ", today + td)

