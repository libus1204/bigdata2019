import re
# 주어진 문자열에서 길이가 1에서 3 사이인 숫자 찾기
text1 = 'Exercises number 1, 12, 13, and 345 are important'
p = re.compile('[\d][\d]?[\d]?')
m1 = p.findall(text1)
for number in m1:
    print(number)
