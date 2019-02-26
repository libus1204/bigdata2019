import re
#  문자열에 모든 공백 없애는 프로그램 작성

text = "how long has this been going on"

p = re.compile(r"\b\w+")
# m = p.sub()
for i in p.findall(text):
    print(i, end="")
