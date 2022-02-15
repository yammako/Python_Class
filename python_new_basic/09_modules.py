# 모듈: 함수, 변수, 클래스를 미리 만들어 둔 python 파일
# 모듈 파일이 다른 폴더에 있을 경우
# import sys
# sys.path.append("파일경로")

import mod1             # 미리 만들어 둔 mod1.py 파일에서 정의한 함수를 사용하겠다는 것
print(mod1.add(1,2))