import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmail.cf", "aaa.exe", "min."]
# p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
p = re.compile(".*[.](?!bat$|exe$).*")
# 유닉스 시스템에서 파일명이 . 으로 끝나는 파일은 필터링 되는 오류가 발생될 수 있다.
# 필터링하고 싶은 확장자의 조건이 추가할수록 정규식은 기하급수적으로 복잡해진다.
for file_name in file_name_list:
    print(p.search(file_name))

# <re.Match object; span=(0, 7), match='foo.bar'>
# None
# <re.Match object; span=(0, 11), match='sendmail.cf'>
# None
# <re.Match object; span=(0, 4), match='min.'>