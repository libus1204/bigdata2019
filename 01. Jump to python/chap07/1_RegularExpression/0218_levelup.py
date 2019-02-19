import re

# p = re.compile('\Apython\s\w+', re.MULTILINE)
#
# data = """python one
# life is too short python is the best program
# python two
# you need python
# python three"""
# #
# # print(p.findall(data))
#
# p = re.compile(r'\Bclass\B')
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))

# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m.group(0))

# p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
# m = p.search("park 010-1234-5678")
# print(m)

# p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
# m = p.search("park 010-1234-5678")
# print(m.group(1))
#
# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())
#
# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-5678")
# print(m.group("name"))
#
# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# print(p.search('Paris in the the spring.').group())
#
# p = re.compile(".+:")
# m = p.search("http://google.com")
# print(m.group())
#
# p = re.compile(".+(?=:)")
# m = p.search("http://google.com")
# print(m.group())
#
# p = re.compile("a[.]{3,}b")
# m = p.match("a...b")
# print(m.group())
#
# p = re.compile('[a-z]+')
# m = p.search("5 python")
# print(m.start()+m.end())
#
# p = re.compile('(blue|white|red)')
# print(p.sub('colour', 'blue socks and red shoes'))


data = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
p = re.compile((r'(\d{4}[-])\d{4}'),re.MULTILINE)
print(p.sub("\g<1>####",data))