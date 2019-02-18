import re

# p = re.compile('[^0]')
# m = p.match('1')
# print(m)
#
# m = p.match('0')
# print(m)

# p = re.compile('[^0-9]')
# m = p.match('1')
# print(m)

p = re.compile('^0')  # caret 은 문자열 클래스 안 에서만 not 의 의미로 사용되는 문법이다.
m = p.match('1')      # 매칭이 되지 않음
print(m)

p = re.compile('^')  # (caret) 은 문자열 클래스 밖에서는 '^' 문자의 의미로 사용된다
m = p.match('^')     # 매칭
print(m)

p = re.compile('[^a-zA-Z0-9]')
m = p.match('7')
print(m)

p = re.compile('[^a-zA-Z09]')
m = p.match('9')
print(m)

p = re.compile('[^a-zA-Z09]')
m = p.match('8')
print(m)
