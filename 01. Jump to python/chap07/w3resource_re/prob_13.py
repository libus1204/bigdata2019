import re
# 'z' 가 포함된 단어를 매치(z를 기준으로 앞 뒤로 공백 없게)
text1 = ' z'
text2 = 'The quick brown fox jumps over the lazy dog.'
p = re.compile('\Bz\B')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
