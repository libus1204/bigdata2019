#  유튭 api 키 :   AIzaSyCrCVODU4fK15oMCa8F2wZv0LwO5J9E4AA

import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver

html = urllib.request.urlopen('https://www.naver.com/')
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)

list = soup.findAll('span', attrs={"class":"ah_k"})
for count in range(1, 21):
    print("%s. "% count +list[count].text )

print("검색할 번호를 입력해주세요 : ",end="")
search_input = int(input(""))
url_search = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
keywords = list[int(search_input)].text
search_site = url_search + "%s" % str(keywords)
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
driver.implicitly_wait(1)
driver.get(search_site)


