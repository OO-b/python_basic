# 로그인 파일의 경로(주소)를 알아서 그 경로로 크롤링 하는 경우 
# BeautifulSoup 사용

import requests
from bs4 import BeautifulSoup
 
login_html = 'https://www.hanbit.co.kr/member/login_proc.php' 
crawl_html = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
 
session_data = requests.session()
 
params = dict()
params['m_id'] = 'wing824'
params['m_passwd'] = '1q2w3e4r'
 
login = session_data.post(login_html, data = params)
login.raise_for_status()
 
#print(login.headers)
#print(session_data.cookies.get_dict())
 
login = session_data.get(crawl_html)
 
soup = BeautifulSoup(login.content, 'html.parser')
 
data = soup.select('dl.mileage_section1 > dd > span')
for item in data:
    print (item.get_text())