import re
#  3, 4, 5글자 모든 문자열 찾기
text = "I was enchanted to meet you"
p = re.compile(r"\b\w{3,5}\b")
m = p.findall(text)
print(m)