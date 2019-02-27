import urllib.request
from bs4 import BeautifulSoup
import re
import csv

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

tags = soup.findAll('div', attrs = {'class':'tit3'})
p_title = re.compile(r'title="(.*)"')
movie_title = p_title.findall(str(tags))  # 영화 제목 정규식으로 찾기
# print(movie_title)

tags_updown = soup.findAll('img', attrs={'class':'arrow'})
movie_rank_updown = []
p_updown = re.compile(r'\balt="(\w+)"')
for count in range(len(tags_updown)):
    if p_updown.findall(str(tags_updown))[count] == "na":
        movie_rank_updown.append("")
    elif p_updown.findall(str(tags_updown))[count] == "up":
        movie_rank_updown.append("+")
    elif p_updown.findall(str(tags_updown))[count] == "down":
        movie_rank_updown.append("-")
# print(movie_rank_updown)  # 영화 랭킹 업다운 부호

tags_num_updown = soup.findAll('td', attrs={'class':'range ac'})
p_num_updown = re.compile(r'ac">(\d{1})<')
movie_rank_updown_num = p_num_updown.findall(str(tags_num_updown))
# print(movie_rank_updown_num) # 영화 랭킹 얼만큼 업다운 됐나 정도

csvfile = open("movie2.csv", 'w', newline="")
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
