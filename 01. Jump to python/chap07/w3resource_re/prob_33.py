import re
#  5글자 모든 문자열 찾기
text = "apple banana cat desk eagle"
p = re.compile(r"\b\w{5}\b")
m = p.findall(text)
print(m)