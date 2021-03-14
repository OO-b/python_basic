# https://pypi.org/ -> pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# pip list -> 현재 설치된 패키지 확인가능 
# pip show beautiful4 -> 해당 패키지 정보 확인가능
# pip install --upgrade beautifulsoup4  해당 패키지 업그레이드
# pip uninstall beautifulsoup4 해당 패키지 삭제