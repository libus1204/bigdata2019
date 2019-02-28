import urllib.request
from bs4 import BeautifulSoup
import re, os, csv

first_dir = 'V2_BigData'
dir_number = 1
dir_name = './naver_ranking'
file_name = '/movie'
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

def search_file_list(dir_name):
    try:
        file_list = os.listdir(dir_name)  # dir_name 폴더 안에 있는 파일을 리스트로 생성
        return len(file_list)  # 그 리스트의 길이를 리턴
    except Exception:
        pass

def search_dir_list(dir_name):
    global dir_number
    dir_name = './naver_ranking%d' % dir_number
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        return dir_number, dir_name
    else:
        file_len = search_file_list(dir_name)
        if file_len < 3:
            return dir_number, dir_name
        else:
            dir_number += 1
            dir_number, dir_name = search_dir_list(dir_name)
            return dir_number, dir_name

if not os.path.isdir(first_dir):
    os.mkdir(first_dir)
os.chdir('./'+first_dir)
dir_number, dir_name = search_dir_list(dir_name)
file_len = search_file_list(dir_name)
file_name = '/movie%d' %((file_len+1)+(dir_number-1)*3)

csvfile = open("%s%s.csv" %(dir_name, file_name), 'w', newline="")
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