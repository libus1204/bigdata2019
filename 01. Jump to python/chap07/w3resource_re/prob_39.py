import re
#  문자열에 공백 없애는 프로그램 작성

text = "see      ya"

p = re.compile(r"([\w]+)\s+([\w]+)")
print(p.sub("\g<1> \g<2>", text))
