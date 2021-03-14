# 패키지 : 모듈을 모아놓은 집합
# 하나의 디렉토리에 여러 모듈을 넣어놓은 것

# 패키지 > 모듈 > 클래스 

# import travel.thailand   #맨뒤에 부분은 항상 모듈이나 패키지만 가능 / 클래스나 함수는 import를 직접할 수 없음
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail() #[태국 패키지 3박 5일 ] 방콕, 파타야 여행 (야시장 투어) 50만원


# #import가 아닌 from ~ import 구문에서는 패키지 사용 가능
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VienamPackage()
# trip_to.detail()



#from random import *
from travel import *  # 이때 package 내에 __init__모듈(__all__)에서 공개 비공개 모듈을 정의해야함
trip_to = vietnam.VienamPackage()
trip_to.detail()

