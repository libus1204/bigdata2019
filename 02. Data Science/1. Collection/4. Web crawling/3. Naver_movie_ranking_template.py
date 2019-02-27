import urllib.request
from bs4 import BeautifulSoup
import csv

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

tags = soup.findAll('div', attrs = {'class':'tit3'})
up_down = soup.find('img', attrs = {'src':'http://imgmovie.naver.net/2007/img/common/icon_na_n1.gif'})
ranking_movie = []
for movie_list in range(len(tags)):
    ranking_movie.append(tags[movie_list].text[1:-1])
tags_ranking = soup.findAll('td', attrs = {'class':'ac'})
rank = []
up_and_down = []
final_rank=[]
final_up_and_down=[]
rank_direct = []
for i in range(len(tags_ranking)):
    if i%3 == 0:
        rank.append(str(tags_ranking[i]))
    elif i%3 == 2:
        up_and_down.append(str(tags_ranking[i]))
    elif i%3 == 1:
        rank_direct.append(str(tags_ranking[i]))
for i in range(len(rank)):
    if i == 9:
        final_rank.append(rank[i][26:28])
    else: final_rank.append(rank[i][25:27])
tags_updown = soup.findAll('img', attrs = {'class':'arrow'})
up_down_again = []
for z in range(len(tags_updown)):
    if tags_updown[z]['alt'] == 'na':
        up_down_again.append('')
    elif tags_updown[z]['alt'] == 'up':
        up_down_again.append('+')
    elif tags_updown[z]['alt'] == 'down':
        up_down_again.append('-')
tags_updown_how = soup.findAll('td', attrs = {'class':'range ac'})
how_updown = []
for y in range(len(tags_updown_how)):
    how_updown.append(tags_updown_how[y].text)
final_list=[]
for count in range(len(ranking_movie)):
    final_list.append(((final_rank[count], ranking_movie[count], up_down_again[count] + how_updown[count])))
csvfile = open("movie.csv", 'w', newline="")
csvwriter = csv.writer(csvfile)
head = ["순위", "영화명", "변동폭"]
csvwriter.writerow(head)
for row in final_list:
    csvwriter.writerow(row)
csvfile.close()

