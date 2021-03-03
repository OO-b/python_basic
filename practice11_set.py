# set : 집합
# 중복이 안됨, 순서가 없음

my_set = {1,2,3,3,3} # {1, 2, 3}
print(my_set)


java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])   # list를 set 으로 감싸서 쓸 수 있음

# 교집합 출력 (java, python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(java는 하지만 python은 하지못하는 개발자)
print(java - python)
print(java.difference(python))

# 교육 후 python 할 줄 아는 사람 늘어남 
python.add("김태호")
print(python)

#java 를 까먹음 
java.remove("김태호")
print(java)