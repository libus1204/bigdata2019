import re
#  문자열의 영,숫자를 제외한 모든 문자열을 제거하는 프로그램 작성

text = "fjie * kelw = woeirj"

p = re.compile("\w+")
for i in p.findall(text):
    print(i, end="")