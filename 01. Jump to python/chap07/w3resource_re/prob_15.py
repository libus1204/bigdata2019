import re
# 특정한 숫자 (ex. 1) 를 시작하는 문자열 매치
text1 = '_1#'
text2 = '1a31_a'
p = re.compile('^1.*')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
