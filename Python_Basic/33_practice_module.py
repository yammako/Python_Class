# 모듈 theater_module.py 파일에 있는 함수를 사용
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

# 모듈명을 줄여서 사용하기
import theater_module as tm
tm.price(3)
tm.price_morning(4)
tm.price_soldier(5)

# 모듈명 없이 사용하기
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# 모듈에서 필요한 함수만 가져다 사용하기
from theater_module import price, price_morning
price(3)
price_morning(4)

from theater_module import price_soldier as price 
price(5)        # price_soldier를 price로 변경해서 사용
