import re
# 문자열이 a로 시작하고 바로 뒤 b가 3번 반복되는 경우
text = 'abbb'
p = re.compile('^ab{3}')
m = p.search(text)
print(m)
