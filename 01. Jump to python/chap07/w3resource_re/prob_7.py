import re
# 문자열에서 언더바와 결합된 소문자 시퀀스
text = 'abbbasdfsa_sawernjhweruiwehuicbv'
p = re.compile('^[a-z]*[_][a-z]*')
m = p.search(text)
print(m)
