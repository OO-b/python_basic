def profile(name, age, main_lang):
    print(name, age, main_lang)



#매개변수를 키워드를 사용해서 넣으면 해당하는 값이 순서상관없이 키워드로 잘 들어간다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바",name="유재석", age=20)