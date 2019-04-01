from urllib.request import urlopen
from bs4 import BeautifulSoup
# 더 페이보릿 : 여왕의 여자  네티즌 리뷰 크롤링
url = 'https://movie.daum.net/moviedb/grade?movieId=119036&type=netizen&page=1'
webpage = urlopen(url)

source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
netizen_reviews = source.findAll('p', {'class': 'desc_review'})

# 1 페이지 네티즌 리뷰 출력
for netizen_review in netizen_reviews:
    print(netizen_review.get_text().strip())

reviews_list = []
for n in range(15):
    url1 = 'https://movie.daum.net/moviedb/grade?movieId=119036&type=netizen&page='
    url2 = n+1
    url = url1+str(url2)
    webpage = urlopen(url)
    source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
    reviews = source.findAll('p', {'class': 'desc_review'})
    for review in reviews:
        reviews_list.append(review.get_text().strip().replace('\n', '').replace('\t', '').replace('\r', ''))

file = open('the-favorite.txt', 'w', encoding='utf-8')

for review in reviews_list:
    file.write(review+'\n')
file.close()
