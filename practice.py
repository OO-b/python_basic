# 자료형 


print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print('나비')
print('ㅋㅋㅋㅋㅋㅋㅋ')
print("ㅋ"*9)

# boolean 참 / 거짓

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not False)
print(not True)
print(not(5 > 10))


# 애완동물을 소개해주세요
animal = "강아지"
name = "연탄이"
age = 4    #정수형은 문자로 바꿔서 출력해야해서 str() 붙여야함
hobby ="산책"
is_adult = age >= 3 # boolean 문자로 바꿔서 출력해야해서 str() 붙여야함

print("우리집 " + animal + "의 이름은 " + name +" 예요")
print("연탄이는 " + str(age) + "살, " + hobby + "좋아함")
print(name +"는 어른일까요?" + str(is_adult))

# 문장 연결은 + / , 로 할 수 있음 
# +로 연결시 str() 사용
# , 로 연결시 str 사용 x 