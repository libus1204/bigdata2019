# #  유튭 api 키 :   AIzaSyCrCVODU4fK15oMCa8F2wZv0LwO5J9E4AA
#
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
# import re
# from selenium import webdriver
#
# html = urllib.request.urlopen('https://www.youtube.com/feed/trending')
# soup = BeautifulSoup(html, 'html.parser')
# tags = str(soup)
#
# p = re.compile(r'<a aria-describedby=.*" class=".*" data-sessionlink=".*" dir=".*" href="(.*)" title="(.*)">.*</a><span class="accessible-')
#
# print("유뷰브 실시간 인기 동영상")
# for count in range(0, 20):
#     print("%s. %s" % (count+1, p.findall(tags)[count][1]))
#     print("주소 : %s" % p.findall(tags)[count][0])
#
# # print("\n시청할 동영상의 번호를 입력해주세요 : ",end="")
# search_input = int(input(""))
# url_search = "https://www.youtube.com"
# keywords = p.findall(tags)[int(search_input)-1][0]
# search_site = url_search + keywords
# driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
# driver.implicitly_wait(1)
# driver.get(search_site)
#
#
import time, sys
for i in range(10):
    sys.stdout.write("\r" + str(i))
    sys.stdout.flush()
    time.sleep(1)