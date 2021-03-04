# 가변인자
# 매개변수를 다르게 하고 싶을때 함수를 더 만들지 않고 사용 하는 방법 


def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end="  ") #end= " "를 넣으면 문장 출력후 계속 한 줄에 출력한다는 내용
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "c", "c++", "c#")
profile("김태호", 25, "kotlin", "swift","", "", "")


def profile1(name, age, *language) :
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end="  ") #end= " "를 넣으면 문장 출력후 계속 한 줄에 출력한다는 내용
    for lang in language :
        print(lang, end="  ")
    print()

profile1("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
profile1("김태호", 25, "kotlin", "swift")
