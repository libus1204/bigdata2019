import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmail.cf", "aaa.exe"]
# p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
p = re.compile(".*[.](?!bat$|exe$).*")
# 확장자의 길이가 3임을 전제로 하기 때문에 '.cf' 와 같이 확장자의 길이가
# 2 인 파일은 필터링되어 실패한 조건이다.
# 유닉스 시스템에서 파일명이 . 으로 끝나는 파일은 필터링 되는 오류가 발생될 수 있다.
# 필터링하고 싶은 확장자의 조건이 추가할수록 정규식은 기하급수적으로 복잡해진다.
for file_name in file_name_list:
    print(p.search(file_name))

# 수행 결과 : 확장자의 글자의 갯수가 2 이상이 되도록 '?'를 추가하여
# ver2 에서 추가한 확장자가 'bat' 인 파일을 제거하기 위한 요구사항을 만족했다.
# <re.Match object; span=(0, 7), match='foo.bar'>
# None
# <re.Match object; span=(0, 11), match='sendmail.cf'>