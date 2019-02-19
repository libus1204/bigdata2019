import re
# 문자열에서 하나의 대문자와 소문자의 연속으로 구성
text = 'AbbbasdfsaWwernjhweruiwehuicbv'
p = re.compile('^[A-Z][a-z]+$')
m = p.search(text)
print(m)
