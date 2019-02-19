import re
# 문자열이 a 로 시작하고 바로 뒤 b가 1번 이상 반복되는 경우
text = 'abbbbasduiosodosdaifjosd'
p = re.compile('^ab+.*$')
m = p.search(text)
print(m)
