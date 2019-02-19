import re
# 매칭할 단어의 첫 글자가 문자열로 되어있는 지 매치(공백x)
text1 = 'apple'
text2 = ' apple'
p = re.compile('^\w+')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
