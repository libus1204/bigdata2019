import urllib.request
from bs4 import BeautifulSoup
import re
import csv

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)

p_title = re.compile(r'<a href="/movie/bi/mi/1. Basic Concept[.]nhn[?]code=\d*"\stitle="(.*)"')
movie_title = p_title.findall(tags)  # 영화 제목 정규식으로 찾기
# print(movie_title)


p_updown = re.compile(r'\balt="([a-z]+)"[ ]class')
rank_updown = p_updown.findall(tags)  # 영화 업엔다운 화살표 찾기
movie_rank_updown = []
for count in range(len(rank_updown)):
    if rank_updown[count] == "na":
        movie_rank_updown.append("")
    elif rank_updown[count] == "up":
        movie_rank_updown.append("+")
    elif rank_updown[count] == "down":
        movie_rank_updown.append("-")
# print(movie_rank_updown)  # 영화 랭킹 업다운 부호


p_num_updown = re.compile(r'range ac">(\d{1})</td>\n')
movie_rank_updown_num = p_num_updown.findall(tags)
# print(movie_rank_updown_num) # 영화 랭킹 얼만큼 업다운 됐나 정도

csvfile = open("movie3.csv", 'w', newline="")
csvwriter = csv.writer(csvfile)
head = ["순위", "영화명", "변동폭"]
csvwriter.writerow(head)
final=[]
num_list=[]
for num in range(1,51):
    num_list.append(num)
for num, name, updown, updown_num in zip(num_list, movie_title, movie_rank_updown, movie_rank_updown_num):
    final.append((num, name, updown+updown_num))
for count in range(len(final)):
    csvwriter.writerow(final[count])
csvfile.close()
