import re
# a로 시작하고 마지막에 b로 끝나는 문자열
text = 'abbasdfsaWwernjhweruiwehuicb'
p = re.compile('^a.*b$')
m = p.search(text)
print(m)
