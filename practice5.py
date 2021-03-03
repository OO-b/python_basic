#문자열 처리함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))  
print(python.replace("Python","Java")) #치환함수 - 대소문자 인식함

index = python.index("n")  # n이 몇번째 위치하는지 
print(index)

index = python.index("n", index + 1) # 두번째 n 이 언제 나오는지
print(index)
print(python.find("n"))  #n을 찾아라

print(python.find("Java")) # -1 : 원하는 값이 해당 내용에 없을경우
#print(python.index("Java")) # error -> 그 밑으로 모든 내용 확인 불가

print("hi")

print(python.count("n")) # 갯수 확인