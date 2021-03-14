# 모듈은 모듈을 쓰려는 파일과 같은 경로에 있거나 같은 폴더에 잇으면 가능함


# import theater_module
# theater_module.price(3) # 3명이서 영화보러 갓을때 가격
# theater_module.price_morning(4) #4명이서 조조할인 영화보러 갔을때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을때


# print("============================================================")
# import theater_module as mv # 별명을 붙여서 줄여서 쓰기 위함 
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# print("============================================================")
# from theater_module import *   
# # from random import *
# # : theater_module  필요없이 모든걸 쓰겠다.

# price(3)
# price_morning(4)
# price_soldier(5)

print("============================================================")
from theater_module import price, price_morning   # 명시적으로 어떤 함수만 가져다 쓸지 정할때 
price(5)
price_morning(6)
price_soldier(7) # 쓸수없음

from theater_module import price_soldier as price #theater_module 에서 price_soldier 함수를 쓰는데 이 함수의 별명을 price로 하겠다.
price(5) #price_soldier 가격이 나옴