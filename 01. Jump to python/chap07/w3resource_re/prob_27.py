import re
# 주어진 문자열 숫자 분리, 출력
text = '1cho la do ahn bo ee myeon 2 leo ke cho jo han de 123hehe 4243'
p = re.compile('\d{1,}')
m = p.findall(text)
for number in m:
    print(number, end=" ")