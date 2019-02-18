import re

original_text ="""1a sdaofsadoifjsoadifjsoaidjf 
b3 asodfijsoaidjfosaidfjsaodfijoasidjre
3k asidjofjoewjir
5j asdifojasdofijasodifjsofd
k4 jfiasdjriejriwejriewkddkdkdkdkdkd
9p sajidrjweiwjrio
u9 jsdiaofjoseijor
"""

# p = re.compile('1a [a-z]+.b3')
p = re.compile("1a [a-z]+.b3", re.DOTALL)
m = p.match(original_text)
print(m)