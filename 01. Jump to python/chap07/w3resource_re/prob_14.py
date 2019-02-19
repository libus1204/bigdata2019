import re
# 대문자, 소문자, 숫자, 언더바만 포함되어 있는 단어 매치
text1 = '_#'
text2 = 'Aa3_a'
p = re.compile('^[a-zA-Z0-9_]*$')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
