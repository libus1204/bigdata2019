import re

p = re.compile('[\d]')  # [0-9]
m = p.match('1')
print(m)                # '1' 로 매칭
m = p.match('5')
print(m)                # '5' 로 매칭

p = re.compile('[\D]')  # [^0-9]
m = p.match('1')
print(m)                # 매칭 되지 않음
m = p.match('5')
print(m)                # 매칭 되지 않음

p = re.compile('[\s]')  # [ ] or re.compile(' ')
m = p.match('1')
print(m)                # 공백이 없으므로 매칭 되지 않음
m = p.match(' 1')
print(m)                # ' ' 로 매칭
m = p.match('   1')
print(m)                # ' ' 로 매칭
m = p.match('''
1''')
print(m)                # '\n' 로 매칭

p = re.compile('[\w]')  # [ ] or re.compile(' ')
m = p.match('1')
print(m)                # '1' 로 매칭
m = p.match('a')
print(m)                # 'a' 로 매칭
m = p.match('K')
print(m)                # 'K' 로 매칭
m = p.match(' ')
print(m)                # 공백이므로 매칭 되지 않음
m = p.match('$')
print(m)                # 특수문자 이므로 매칭 되지 않음
m = p.match('-')
print(m)                # 특수문자 이므로 매칭 되지 않음
