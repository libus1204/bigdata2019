from  bs4 import BeautifulSoup
import urllib.request
import re

print("1. TOP 20 국내\n2. TOP 20 해외")
menu_music = input("번호를 선택하세요 : ")
if menu_music == '1':
    html = urllib.request.urlopen('https://music.naver.com/listen/top100.nhn?domain=DOMESTIC_V2')
    soup = BeautifulSoup(html, 'html.parser')
    tags = str(soup)
    korean_sing_title_list = []
    korean_singer_list = []
    p_korean_title = re.compile(r'class="_title title.*title=".*psis">(.*)</span>')
    for titles in p_korean_title.findall(tags):
        korean_sing_title_list.append(titles)
    p_korean_singer = re.compile(r'" title="(.*)">\n')
    p_korean_artist = re.compile(r'" href="(.*)" title=".*">\n')
    artist_info = p_korean_artist.findall(tags)
    music_url = "https://music.naver.com"
    print(music_url+artist_info[1])
    for singer in p_korean_singer.findall(tags):
        if singer == '자동완성 펼치기':
            pass
        else: korean_singer_list.append(singer)
    # print(korean_singer_list)
    # print(korean_sing_title_list)
if menu_music == '2':
    html = urllib.request.urlopen('https://music.naver.com/listen/top100.nhn?domain=OVERSEA_V2')
    soup = BeautifulSoup(html, 'html.parser')
    tags = str(soup)
    pop_title_list = []
    pop_singer_list = []
    p_pop_title = re.compile(r'<span class="ellipsis">(.*)</span></a>')
    for pop_titles in p_pop_title.findall(tags):
        pop_title_list.append(pop_titles)
    p_pop_singer = re.compile(r'" title="(.*)">\n')
    for pop_singer in p_pop_singer.findall(tags):
        if pop_singer == '자동완성 펼치기':pass
        else: pop_singer_list.append(pop_singer)

