# pickle : 프로그램상에서 사용하는 데이터를 파일형태로 저장 

import pickle
# profile_file = open("profile.pickle", "wb") # w 쓰기 b binary / pickle은 인코딩 설정 굳이 x
# profile = {"이름": "박명수", "나이":30, "취미":["축구","골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를  file에 저장    #피클을 이용해서 이 내용을 파일에다 쓰는 행위 : dump
# profile_file.close()

profile_file = open("profile.pickle", "rb") # 읽기
profile = pickle.load(profile_file) # file에 있는 정보를 데이터형태(profile)로 불러와줌
print(profile)
profile_file.close()
