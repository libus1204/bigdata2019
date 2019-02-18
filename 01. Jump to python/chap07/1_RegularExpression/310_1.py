import re

# p = re.compile("^python\s\w+")
p = re.compile("\w+\spython$", re.MULTILINE)

data = """python one python debug
life is too short
python two
you need python
python three
I will study python"""

print(p.findall(data))