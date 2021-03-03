# 슬라이싱

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("년 : " + jumin[0:2]) # 0 부터 2직전까지 (0, 1)
print("월 : " + jumin[2:4]) 
print("월 : " + jumin[4:6]) 

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " +  jumin[7:])   # jumin[7:] =  jumin[7:14] 7부터 끝까지

print("뒤 7자리 (뒤에서부터) " + jumin[-7:] ) # 맨뒤에서 7번째 부터 끝까지 (-1부터 셈)