import re
#  모든 공백, 쉼표, 점을 콜론으로 대체
text = 'blank is what this is _ is underbar and ..., is Idk what it is..'
p = re.compile('\s|[,]|[.]')
print(p.sub(':', text))
