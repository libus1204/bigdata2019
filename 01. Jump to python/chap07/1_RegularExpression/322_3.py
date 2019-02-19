import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmail.cf"]
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])$")
for file_name in file_name_list:
    print(p.search(file_name))

# 수행 결과 : 확장자가 bar 인 문자열을 필터링 하지 않기 위한 '|' 조건이
# 확장자의 길이가 3임을 전제로 하기 때문에 '.cf' 와 같이 확장자의 길이가
# 2 인 파일은 필터링되어 실패한 조건이다.
# <re.Match object; span=(0, 7), match='foo.bar'>
# None
# None