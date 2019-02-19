import re
#  'Road' 를 'Rd'로 축약하는 프로그램
text = 'Road'
p = re.compile('[oa]')
print(p.sub('', text))
