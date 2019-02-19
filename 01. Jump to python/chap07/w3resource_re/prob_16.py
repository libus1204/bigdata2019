import re
# IP 주소에서 0을 없애는 프로그램
text = '111.022.033.044'
p = re.compile('[0]*(\d*)')
ip_address = p.sub('\g<1>',text)
print(ip_address)

