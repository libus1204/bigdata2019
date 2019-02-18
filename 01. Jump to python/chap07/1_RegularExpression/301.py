import re

# p = re.compile('ca{2}t')  # [] 숫자가 한 개만 올 때는 해당 반복수를 정확히 지킨 문자열만 매칭
# m = p.match('ct')
# print(m)
# m = p.match('cat')
# print(m)
# m = p.match('caat')
# print(m)
# m = p.match('caaat')
# print(m)
#
# p = re.compile('ca{2,5}t')  # a 가 2~5 사이의 반복인 경우에 매칭이 된다.
# m = p.match('cat')
# print(m)
# m = p.match('caat')
# print(m)
# m = p.match('caaat')
# print(m)
# m = p.match('caaaaat')
# print(m)
# m = p.match('caaaaaaaat')
# print(m)

# p = re.compile('ca{2,}t')  # a 가 2 이상 반복인 경우 매칭
# m = p.match('cat')
# print(m)
# m = p.match('caat')
# print(m)
# m = p.match('caaat')
# print(m)
# m = p.match('caaaaat')
# print(m)
# m = p.match('caaaaaaaat')
# print(m)

p = re.compile('ca{,5}t')  # a 가 5 이하 반복인 경우 매칭
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaat')
print(m)
m = p.match('caaaaat')
print(m)
m = p.match('caaaaaaaat')
print(m)

