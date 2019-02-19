import re
# 문자 단어들 리스트 중, 단어 둘다 'P' 문자로 시작하는 경우 출력
words_list = ['Pineapple Pay', 'Pen pineapple', 'Apple pen']
p = re.compile('^P\w+\sP\w+$')
for capital_p in words_list:
    m = p.match(capital_p)
    if m: print(capital_p)






