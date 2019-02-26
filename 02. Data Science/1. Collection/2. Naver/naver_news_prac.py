import re

text = "http://blog.naver.com/selene8989?Redirect=Log&amp;logNo=221470512378"
# p = re.compile("\?Redirect=Log&amp;logNo=")
print(re.sub("\?Redirect=Log&amp;logNo=", '/', text))
# print(p.findall(text))

# print(p.findall(text))