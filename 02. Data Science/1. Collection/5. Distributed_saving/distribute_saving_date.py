import urllib.request
from bs4 import BeautifulSoup
import re, os, time, csv

dir_num = 1
dir_name = './naver_ranking1'
file_name = '/movie1'
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
p=re.compile(r'title="(.+)">\1</a>\n</div>\n</td>\n.+\n.+\n<td class="ac">.+alt="([a-z]+)".+\n<td class=.+(\d+)')

def search_file_list(dir_name):
    try:
        file_list = os.listdir(dir_name)  # dir_name 폴더 안에 있는 파일을 리스트로 생성
        return len(file_list)  # 그 리스트의 길이를 리턴
    except Exception:
        pass

def search_dir_list(dir_name):
    global dir_num   # dir_num 값 1 을 전역변수로 참조
    dir_name = './naver_ranking%d' % dir_num  #  폴더 이름은 ./naver_ranking%d << 첨에는  %d가 1로 들어감
    if not os.path.isdir(dir_name):  # ./naver_ranking%d 이 존재하는지 확인, 없다면
        os.mkdir(dir_name)           # ./naver_ranking%d 을 생성
        return dir_num, dir_name   # dir_num 은 폴더 갯수, dir_name 은 ./naver_ranking%d 리턴
    else:   # ./naver_ranking%d 이 존재한다면
        file_len = search_file_list(dir_name)   # ./naver_ranking% 의 폴더 안에 있는 파일을 리스트로 만들고, 길이 값을 file_len 에 저장
        if file_len < 3:  # 그 길이 값이 3 이하이면
            return dir_num, dir_name  # dir_num, dir_name 리턴(파일이 3개 이하면 계속 그 폴더이도록)
        else:  # 리스트 길이 값이 3 이상 이면
            dir_num += 1  # 폴더 이름이 1 증가
            dir_num, dir_name = search_dir_list(dir_name)  # 폴더 이름 1 증가한 폴더를 만들고, 그 num과 이름 저장
            return dir_num, dir_name  # 위에 값 리턴

dir_num, dir_name = search_dir_list(dir_name)  # 폴더 이름, 뒤에 숫자 저장
file_name = './%s' % (time.strftime('%Y-%m-%d_%H%M%S', time.localtime()))

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