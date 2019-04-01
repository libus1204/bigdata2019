from collections import Counter
from konlpy.tag import Okt

# prac1 에서 만든 댓글 파일 호출
file = open('the-favorite.txt', 'r', encoding='utf-8')
lines = file.readlines()

# 전체 댓글을 다시 저장
favorite = []
for line in lines:
    favorite.append(line)
file.close()

# konlpy 모듈 호출
okt = Okt()

# 각 문장별로 형태소 구분하기
sentence_tag = []
for sentence in favorite:
    morph = okt.pos(sentence)
    sentence_tag.append(morph)
    # print(morph)
    # print('-'*30)

print(sentence_tag)
print(len(sentence_tag))
print('\n'*3)

# 명사만 구별해 리스트 담기
noun_list = []
for sentences in sentence_tag:
    for word, tag in sentences:
        if tag in ['Noun']:
            noun_list.append(word)

# 선별도니 명사 빈도수 계산 / 상위 빈도 10개 까지 출력
counts = Counter(noun_list)
print(counts.most_common(10))
