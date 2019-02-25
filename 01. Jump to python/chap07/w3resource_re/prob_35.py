import re
#  문자열에 적어도 4개 이상의 단어를 찾는 프로그램 작성
p = re.compile(r"\b\w{4,}\b")
text = "This night is sparkling don't you let it go"
print(p.findall(text))
