# key value  - key 값은 숫자 / 문자 모두 가능 
# 사전에서는 키에대한 중복이 허용되지 않음

cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) #none
print(cabinet.get(5), "사용가능") # 값이없으면 뒤에 값 줌

#print(cabinet[5])  # error

print(3 in cabinet) # return boolean key in 변수 : key가 변수안에 있는가?
print(5 in cabinet) 


cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # 중복되는 키값이면 원래 있던 내용이 사라지고 덮어씀
cabinet["C-20"] = "조세호"
print(cabinet)


# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())


#목욕탕 폐점
cabinet.clear()
print(cabinet)