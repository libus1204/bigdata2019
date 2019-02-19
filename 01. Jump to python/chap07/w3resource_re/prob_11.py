import re
# 매칭할 text 맨 끝에 .로 끝나게, 공백x
text1 = 'apple.'
text2 = 'apple. '
p = re.compile('.+[.]\S*$')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
