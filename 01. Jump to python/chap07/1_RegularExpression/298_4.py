import re

original_text ="""K1 sdaofsadoifjsoadifjsoaidjf  # 대문자라 매칭 안됨
b3 asodfijsoaidjfosaidfjsaodfijoasidjre
3k asidjofjoewjir
5j asdifojasdofijasodifjsofd
k4 jfiasdjriejriwejriewkddkdkdkdkdkd
9p sajidrjweiwjrio
u9 jsdiaofjoseijor
"""

# p = re.compile('[a-z][0-9]')       # 매칭 되지 않음
# p = re.compile('[a-zA-Z][0-9]')    # 'K1' 로 매칭
# p = re.compile('[a-zA-Z0-9][0-9]') # 'K1' 로 매칭
p = re.compile('[a-zA-Z0-9][0-9]')  # 'K1' 로 매칭
m = p.match(original_text)
print(m)