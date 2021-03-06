import urllib.request
from bs4 import BeautifulSoup
import re, csv

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)

p_all = re.compile(r'''
#
<.*>\n<.*>\n
#title
<.*title="(.*)">
.*</a>\n</div>\n</td>\n.*\n.*\n
#등락
<.*alt="(.{2,4})".*\n<.*>
#등락폭
(\d+)<.*>''',re.VERBOSE)

movie_all_find = p_all.findall(tags)
movie_title=[]
movie_rank_updown=[]
movie_rank_updown_num=[]
for num in range(len(movie_all_find)):
    movie_title.append(movie_all_find[num][0])
    movie_rank_updown_num.append(movie_all_find[num][2])
    if movie_all_find[num][1] == "na":
        movie_rank_updown.append("")
    elif movie_all_find[num][1] == "up":
        movie_rank_updown.append("+")
    elif movie_all_find[num][1] == "down":
        movie_rank_updown.append("-")

csvfile = open("movie4.csv", 'w', newline="")
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
