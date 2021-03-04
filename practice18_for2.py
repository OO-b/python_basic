# 출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104 

studnets = [1,2,3,4,5]
print(studnets)
studnets = [i+100 for i in studnets] #students에서 값을 불러와서 i에 넣을건데 거기에 i+100씩해서 students 배열로 다시 만들거야.
print(studnets)

# 학생 이름을 길이로 변환
studnets = ["Iron man", "Thor", "I am groot"]
print(studnets)

studnets = [len(i) for i in studnets]
print(studnets)

studnets = ["Iron man", "Thor", "I am groot"]
studnets = [i.upper() for i in studnets]
print(studnets)
