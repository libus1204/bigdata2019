import re
# 문자열 끝에 숫자를 검사하는 프로그램
text1 = 'asdfosjidf2'
text2 = 'vfkdkdkd'
p = re.compile('.*[\d]$')
m1 = p.search(text1)
m2 = p.search(text2)
print(m1)
print(m2)
