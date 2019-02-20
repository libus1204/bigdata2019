import re

p = re.compile('.*@.*[.](?=com$|net$).*$')
m = p.match('park@naver.com')
print(m)
m = p.match('kim@daum.net')
print(m)
m = p.match('lee@myhome.co.kr')
print(m)