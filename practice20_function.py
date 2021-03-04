# 함수 정의
def open_account() :
    print("새로운 계좌가 생성되었습니다.")

# 함수 출력
open_account()

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money 


def withdraw(balanc, money) : #출금

    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액이 {0}원 입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 불가능합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100
    return commission, balance - money - commission   # 두개의 값을 , 로 -> 튜플형식 


balance = 0 # 잔액

balance = deposit(0, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))
print(balance)