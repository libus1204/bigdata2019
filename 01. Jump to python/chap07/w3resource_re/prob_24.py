import re
# URL 에서 년, 월, 일 추출하는 프로그램
url = 'http://news.chosun.com/site/data/html_dir/2019/02/19/2019021901408.html'
p = re.compile('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})')
m = p.search(url)
print("year : %s" %m.group(1))
print("month : %s" %m.group(2))
print("day : %s" %m.group(3))







