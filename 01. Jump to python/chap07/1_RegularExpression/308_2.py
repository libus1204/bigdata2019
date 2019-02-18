import re

original_text = """aasdfdf
 fdsfdfb"""
# p = re.compile("[a-z]*. [a-z]*")
p = re.compile("[a-z]*. [a-z]*", re.DOTALL)
m = p.match(original_text)
print(m)

