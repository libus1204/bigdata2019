import re
# 문자열에 a로 시작하고 그 뒤에 b가 0 번 이상 반복되는 경우
text = 'abbbfdsac'
p = re.compile('^ab*')
m = p.search(text)
print(m)
