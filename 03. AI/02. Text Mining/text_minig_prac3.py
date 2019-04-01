import pytagcloud
import random
import webbrowser
from konlpy.tag import Okt
from collections import Counter

####################################################
# get_tags 새함수 만듦:
# 기능 1. 댓글별로 명사만 추출
# 기능 2. 명사 빈도수 집계
# 기능 3. 단어구름에 표시할 명사에 3가지 시각화 속성
#        (색상'color', 단어'tag', 크기'size')부여

# 입력변수- text : 댓글, ntags : 표시할 단어수, multiplier : 크기가중치

def get_tags(text, ntags=20, multiplier=5):
    okt = Okt()
    nouns = []
    # 명사만 추출, noun 변수에 누적해 저장
    for sentence in text:
        for noun in okt.nouns(sentence):
            nouns.append(noun)
            count = Counter(nouns)
    return [{'color': color(), 'tag': n, 'size': 2*c*multiplier} for n, c in count.most_common(ntags)]

# draw_cloud 새함수 만듦:
# 기능 1. pytagclud 모듈을 사용해 단어구름 이미지를 만듦
# 기능 2. 단어구름 이미지를 파일로 저장함
# 기능 3. 화면에 단어구름을 표시함

# 입력변수 tags : get_tags()에서 리턴되는 color, tag, size(이미지크기) 값이 전달됨.
# fontname : Noto Sans CJK - 한글폰트

def draw_cloud(tags, filename, fontname = 'Noto Sans CJK', size1 = (1300, 800)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size1)
    # 저장된 단어구름 이미지파일(wc1.png)을 내 컴퓨터에 띄움
    webbrowser.open(filename)

####################################################
# 명사에 적용할 색상 랜덤지정
r = lambda: random.randint(0, 255)
color = lambda: (r(), r(), r())

favorite = []
file = open('the-favorite.txt', 'r', encoding='utf-8')
lines = file.readlines()

for line in lines:
    favorite.append(line)
file.close()


# 댓글 명사 추출 및 빈도분석 실시
tags = get_tags(favorite)
print(tags)
draw_cloud(tags, 'wc1.png')
