#비교연산자


print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 나머지구하기 1

print(5//3) # 몫 구하기 1

print( 10 > 3)
print(4 >= 7)

print(3 == 3) #같다

print(1 != 3) #같지않다   답 :True

print(not(1 != 3 )) #false

print(( 3> 0) and (3 <5))  #true
print(( 3> 0) & (3 <5))  #true

print((3 >0 ) or (3 >5)) 
print((3 >0 ) | (3 >5)) 

print(5 > 4 > 3) # True
print(5 > 4 > 7)  # False



#간단한 수식
number = 2+3*4
print(number)
number = number +2
print(number)
number += 2  #number = number +2
print(number)
number *= 2 #number = number  *2
print(number)
number /= 2 #number = number  /2
print(number)
number -= 2 #number = number - 2
print(number)

number %= 5  #나머지
print(number)