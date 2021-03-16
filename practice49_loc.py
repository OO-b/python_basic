# inspect  모듈 /패키지 위치 확인 가능

import inspect
import random
print(inspect.getfile(random))

from travel import * 
print(inspect.getfile(thailand))
trip_to = vietnam.VienamPackage()
trip_to.detail()