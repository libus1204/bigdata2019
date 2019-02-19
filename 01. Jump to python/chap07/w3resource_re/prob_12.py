import re
# 'z' 가 포함된 단어를 매치
text1 = 'applez'
text2 = 'The quick brown fox jumps over the lay dog.'
p = re.compile('z')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
