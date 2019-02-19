import re
# 문자열이 a로 시작하고 그 후 b가 0~1 번 반복되는 경우
text = 'abbbfasdfsadb'
p = re.compile('^ab?')
m = p.search(text)
print(m)
