import re
#  5글자 모든 문자열 찾기
text = "apple banana cat desk eagle"
p = re.compile("\w{5}")
m = p.findall(text)
print(m)

