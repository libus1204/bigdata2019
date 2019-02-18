import re

p = re.compile('ab?c')  # a 다음 b 가 0 또는 1 번 반복 되어야 매칭
m = p.match('ac')       # b 가 0번 반복됨. 매칭
print(m)
m = p.match('abc')      # b 가 1번 반복됨. 매칭
print(m)
m = p.match('abbc')     # b 가 2번 반복됨. 매칭 되지 않음
print(m)
m = p.match('abbbcd')
print(m)
m = p.match('abcd')     # abc 매칭.
print(m)