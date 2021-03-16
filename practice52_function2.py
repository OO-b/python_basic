# 외장함수
# : 직접 import를 해서 써야하는 함수 

# google -> list of python modules


# =================== 몇가지 내장함수 사용해보기 =============================

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py"))

# -------------------------------------------------

# os : 운영체제에서 제공하는 기본기능
import os
print(os.getcwd()) #현재디렉토리  

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else :
    os.makedirs(folder) #폴더생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # 폴더 내에 모든 파일

# -------------------------------------------------

# time :시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

#timedelta : 두 날짜 사이의 간격을 알려 줌 
today = datetime.date.today() # 오늘날짜 저장
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난지 100일은",  today + td) #오늘부터 100일 후 