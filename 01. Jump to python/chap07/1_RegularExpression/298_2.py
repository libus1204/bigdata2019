import re

p = re.compile('[a-c]')
m = p.match("a")
print(m)  # 'a' 로 매칭

p = re.compile('[a-c]')
m = p.match("b")
print(m)  # 'b' 로 매칭

p = re.compile('[a-c]')
m = p.match("c")
print(m)  # 'c' 로 매칭

p = re.compile('[1-3]')
m = p.match("1")
print(m)  # '1' 로 매칭

p = re.compile('[1-3]')
m = p.match("2")
print(m)  # '2' 로 매칭

p = re.compile('[1-3]')
m = p.match("3")
print(m)  # '3' 로 매칭
