# 튜플 
# list 와 달리 내용 변경 추가 불가능
# 속도가 list 보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") X 불가능 

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")    # 한번에 넣을 수 있음
print(name, age, hobby)