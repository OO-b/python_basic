#. 지역변수(함수내에서만) 전역변수(프로그램 내에서 어디서든 부를 수 있는)

gun = 10 

def checkpoint(soldiers) : # 경계근무
        global gun # 전역공간에 있는 gun 사용
        gun = gun - soldiers
        print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers): #gun  지역변수
    gun = gun - soldiers 
    return gun #  전역으로 쓰려면 리턴시켜서 밖에서 변수로 받으면 됨

print("전체 총 :{0}".format(gun))
checkpoint(2) # 2명이 경계 근무나감
gun = checkpoint_ret(gun, 2)
print("남은 총 :{0}".format(gun))
