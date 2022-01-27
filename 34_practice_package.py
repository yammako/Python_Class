# 패키지 (모듈을 모아둔 집합)
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__       __init__.py에 패키지를 작성
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 패키지가 동일한 경로에 있지 않을 때
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))