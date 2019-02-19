import re
# yyyy-mm-dd 형식의 날짜를 dd-mm-yyyy 형식으로 변환하는 프로그램
birthday = '1990-12-04'
p = re.compile('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
m = p.search(birthday)
print(birthday)
print(m.group(3)+"-"+m.group(2)+"-"+m.group(1))







