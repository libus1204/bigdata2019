import re
#  따옴표 안에 문자열 찾기
text = '"This", "was", "the", "very", "first", "page"'
p = re.compile(r'"([\w]*)"')
print(p.findall(text))
