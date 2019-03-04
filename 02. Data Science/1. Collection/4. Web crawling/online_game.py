from  bs4 import BeautifulSoup
import urllib.request
import re

html = urllib.request.urlopen("http://www.online-gameranking100.com/bbs/board.php?bo_table=online")
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)
online_game_title = []
p_online_title = re.compile(r'id=\d\d\d"><span>(.*)</span></a>')
for count in range(len(p_online_title.findall(tags))):
    online_game_title.append(p_online_title.findall(tags)[count])
online_game_site = []
p_online_site = re.compile(r'bookmarksite.*(http.*'')[)]')
for count2 in range(len(p_online_site.findall(tags))):
    online_game_site.append(p_online_site.findall(tags)[count2])
print(online_game_site)
print(online_game_title)