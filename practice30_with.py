# with : 파일을 조금 더 편하게 작업 가능

# import pickle
# with open("profile.pickle", "rb") as profile_file:  # profile.pickle 파일을 열어서  profile_file 이 변수에 저장
#     print(pickle.load(profile_file))    # profile_file 파일의 내용을 pickle의 load를 이용해서 불러와서 사용
#     # close 필요  x



    # with open("study.txt", "w", encoding="utf8") as study_file:
    #     study_file.write("파이선을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file :
    print(study_file.read())