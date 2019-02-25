import re
#  스네이크 케이스 문자열을 마켈 케이스 문자열로 변환하는 프로그램 작성
#  카멜 케이스 : 두 단어 이상의 조합을 대문자로 구분하는 것 (ex isHouse DoSomething)
#  스네이크 케이스 : 두 단어 이상의 조합을 _ 로 구분하는 것 (ex is_house Do_Something)
text = "sleeps_well"
p = re.compile('[a-z]+')
for i in range(len(p.findall(text))):
    p.findall(text)[0].capitalize()