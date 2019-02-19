import re

p = re.compile('\section')     # \s 가 공백문자를 표현하는 정규식이기 때문에
print(p.search('\section'))    # Not match
p = re.compile('\\section')    # 정규식에서는 '\\'을 '\'로 인식하지 않는다.
print(p.search('\section'))
p = re.compile(r'\section')
# 정규식에서는 raw string 포맷을 사용해도 '\' 한계는 문자로 인식하지 않는다.
print(p.search('\section'))
p = re.compile(r'\\section')
# raw string 문법으로 보면 r'\\'은 '\\\\' 의미이지만
# 아래 '\'가 한 개인 string 에도 매치가 된다.
print(p.search('\section'))
p = re.compile('\\\\section')
print(p.search('\section'))
p = re.compile(r'\\section')
print(p.search('\\section'))