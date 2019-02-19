import re
# 주어진 문자열의 숫자와 그 위치를 분리, 출력
text = 'The following example creates an A24rrayList with a capacity of 50 elements. Four elements are blah blah'
p = re.compile('\d+')
m = p.finditer(text)
for count in m:
    print(count.group()+" is started at %d." %(count.start()))
