# 사이트로 접속해서 사용하는 크롤링 하는 방법 
# selenium 사용 

import time
import os
from selenium import webdriver

folder_dt= 'c:\\iyiy\\Earth\\korea\\seoul\\dong\\' + time.strftime('%Y\%m\\')  # 폴더루트 

if not os.path.exists(folder_dt):  # os 라이브러리 사용 -> 폴더가 없다면 폴더를 만들도록
    os.makedirs(folder_dt)

# chromedriver 경로를 인자값으로 넘겨줌
# 같은 경로에 chromedriver.exe 있을 경우 경로 입력 필요 없음.

try :
    options = webdriver.ChromeOptions()
    options.add_argument("headless")   # 위에 두줄 브라우저 안켜지게 하는것 

    chrome_loc = "C:\chromedriver.exe" # chromeDriver.exe 설치 위치
    url = "http://iplug.dasstech.com/login" # 크롤링할 사이트 주소


    browser = webdriver.Chrome(chrome_loc, options=options)# "./chromedriver.exe"

    # 1. 사이트 이동
    browser.get(url)

    # 2. (네이버)로그인 버튼 클릭
    #elem = browser.find_element_by_class_name("link_login")
    #elem.click()

    # 3. id, pw 입력
    browser.find_element_by_id("id").send_keys("해당아이디")
    browser.find_element_by_id("pass").send_keys("해당비밀번호")


    # 4. 로그인 버튼 클릭
    browser.find_element_by_tag_name("button").click()

    time.sleep(3)

    current_url = browser.current_url #로그인 후 현재 브라우저 주소 확인 가능

        f = open(folder_dt + time.strftime('%d')+'.txt', 'w')

        f.write("[inverter]\n")
        f.write("현재발전량=0\n")
        f.write("금일발전량=0\n")
        f.write("전일발전량=0\n")
        f.write("누적발전량=0\n")
        f.write("금일CO2저감량=0\n")
        f.write("누적CO2저감량=0\n")
        f.write("인버터상태=1\n")
        f.write("웹접속상태=0")

        f.close()



except Exception as err:

    print(err)

    f = open(folder_dt + time.strftime('%d')+'.txt', 'w')

    f.write("[inverter]\n")
    f.write("현재발전량=0\n")
    f.write("금일발전량=0\n")
    f.write("전일발전량=0\n")
    f.write("누적발전량=0\n")
    f.write("금일CO2저감량=0\n")
    f.write("누적CO2저감량=0\n")
    f.write("인버터상태=1\n")
    f.write("웹접속상태=0")

    f.close()

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
#browser.find_element_by_id("id").clear()
#browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력

currentPower = browser.find_element_by_css_selector("#inverter_scroll .power").text[:-2]# 현재발전량
todayPower = browser.find_element_by_id("todayPower").text # 금일발전량
previosDayPower =  browser.find_element_by_id("previosDayPower").text # 전일발전량 
accumulatePower = browser.find_element_by_id("accumulatePower").text# 누적발전량 
currentCo2Power = browser.find_element_by_id("currentCo2Power").text # 금일 CO2 저감량 
accumulateCo2Power = browser.find_element_by_id("accumulateCo2Power").text # 누적 CO2 저감량 
inverterstatus = browser.find_element_by_css_selector("#inverter_scroll .status").text[2:] # 인버터 상태 

if inverterstatus=="RUN" :
    inverterstatus = 0
elif inverterstatus=="FAULT" :
    inverterstatus = 1
elif inverterstatus=="OFF" :
    inverterstatus = 2
elif inverterstatus == "STOP" :
    inverterstatus = 3

#f = open(time.strftime('%Y-%m-%d %H_%M_%S')+' seoul.txt', 'a')
#f = open(time.strftime('%Y-%m-%d')+' seoul.txt', 'w')

f = open(folder_dt + time.strftime('%d')+'.txt', 'w')


f.write("[inverter]\n")
f.write("현재발전량="+currentPower+"\n")
f.write("금일발전량="+todayPower+"\n")
f.write("전일발전량="+previosDayPower+"\n")
f.write("누적발전량="+accumulatePower+"\n")
f.write("금일CO2저감량="+currentCo2Power+"\n")
f.write("누적CO2저감량="+accumulateCo2Power+"\n")
f.write("인버터상태="+str(inverterstatus)+"\n")
f.write("웹접속상태=1")
f.close()


# 7. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료