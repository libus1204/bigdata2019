import re
# 주어진 문자열 'a' 또는 'e'로 시작하는 모든 단어 찾기
text = 'apple banana cat desk elephant angel needs elegance'
p = re.compile('[a]\w*|[e]\w*')
m = p.findall(text)
for word in m:
    print(word, end=" ")

