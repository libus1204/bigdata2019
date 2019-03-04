from  bs4 import BeautifulSoup
import urllib.request
import re

html = urllib.request.urlopen("https://map.naver.com/local/siteview.nhn?code=13479597")
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)
print(tags)
