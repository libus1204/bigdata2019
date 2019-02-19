import re
# 공백을 언더바로, 언더바를 공백으로
text = 'abc abd abe'
p = re.compile('\s')
print(p.sub('_', text))
text = 'abc_abd_abe'
p = re.compile('[_]')
print(p.sub(' ', text))


