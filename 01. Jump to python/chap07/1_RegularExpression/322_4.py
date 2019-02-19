import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmail.cf"]
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
for file_name in file_name_list:
    print(p.search(file_name))

# 수행 결과 : 확장자의 글자의 갯수가 2 이상이 되도록 '?'를 추가하여
# ver2 에서 추가한 확장자가 'bat' 인 파일을 제거하기 위한 요구사항을 만족했다.
# <re.Match object; span=(0, 7), match='foo.bar'>
# None
# <re.Match object; span=(0, 11), match='sendmail.cf'>