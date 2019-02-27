import urllib.request
from bs4 import BeautifulSoup
import re
import csv

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)

# p_title = re.compile(r'<a href="/movie/bi/mi/basic[.]nhn[?]code=\d*"\stitle="(.*)"')
# movie_title = p_title.findall(tags)  # 영화 제목 정규식으로 찾기
# # print(movie_title)
#
#
# p_updown = re.compile(r'\balt="([a-z]+)"[ ]class')
# rank_updown = p_updown.findall(tags)  # 영화 업엔다운 화살표 찾기
# movie_rank_updown = []
# for count in range(len(rank_updown)):
#     if rank_updown[count] == "na":
#         movie_rank_updown.append("")
#     elif rank_updown[count] == "up":
#         movie_rank_updown.append("+")
#     elif rank_updown[count] == "down":
#         movie_rank_updown.append("-")
# # print(movie_rank_updown)  # 영화 랭킹 업다운 부호
#
#
# p_num_updown = re.compile(r'range ac">(\d{1})</td>\n')
# movie_rank_updown_num = p_num_updown.findall(tags)
# # print(movie_rank_updown_num) # 영화 랭킹 얼만큼 업다운 됐나 정도


# p_all = re.compile(r'<.*>\n<.*>\n<.*title="(.*)">.*</a>\n</div>\n</td>\n.*\n.*\n<.*alt="(.{2,4})".*\n<.*>(\d+)<.*>')
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

# print(movie_title)
# print(movie_title)
# print(len(movie_all_find))

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
