def profile(name, age, main_lang) :
    print("이름 :{0}  \t 나이 : {1} \t 주 사용 언어: {2}" \
        .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 20, "자바")

# 같은학교 같은학년 같은반 같은수업이라면?
def profile(name, age=17, main_lang="파이썬") : #전달받지 않았을 경우에는 기본으로 넣을 값을 지정
    print("이름 :{0}  \t 나이 : {1} \t 주 사용 언어: {2}" \
        .format(name, age, main_lang))


profile("유재석")
profile("김태호")

