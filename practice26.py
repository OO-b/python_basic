# 표준 입출력

print("python","java")
print("python","java", sep=",")
print("python","java", "javascript",sep=" vs ")

print("python","java", sep=",", end="?")
print("무엇이 더 재밌을까요?")




import sys
print("python","java", file=sys.stdout) #표준출력으로 문장이 찍힘 
print("python","java", file=sys.stderr) #표준에러로 처리됨 (log처리시 확인)



# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score) 
    print(subject.ljust(8), str(score).rjust(4), sep=":") #8개 공간 확보 후 왼쪽정렬, 4개 공간 확보 후 오른쪽정렬    // 수학       0




# 은행 대기순번표
# 001, 002, 003
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3))




# 표준입력
#사용자 입력 통해서 입력을 받으면 무조건 문자열로 인식함

answer = input("아무값이나 입력하세요 :")  
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")