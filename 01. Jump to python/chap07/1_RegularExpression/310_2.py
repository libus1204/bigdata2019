import re

p = re.compile("python", re.MULTILINE)  # findall 의 결과와 동일한 효과

data = """python one python debug
life is too short
python two
you need python
python three
I will study python"""

m = p.findall(data)
print(m)