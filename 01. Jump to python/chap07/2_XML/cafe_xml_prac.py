import re
from xml.etree.ElementTree import parse
tree = parse("students_info.xml")
root = tree.getroot()
name = []
sex = []
age = []
major = []
computer_language_name = []
computer_language_level = []
computer_language_value = []
computer_language_name_count_order = []
for information in root:
    name.append(information.get("name"))
    sex.append(information.get("sex"))
for information in root.findall("student"):
    age.append(information.findtext("age"))
    major.append(information.findtext("major"))
    for information2 in information.findall("practicable_computer_languages"):
        computer_language_name_count = 0
        if not information2:
            computer_language_name_count += 1
            computer_language_name.append("None")
            computer_language_level.append("None")
            computer_language_value.append("None")
        for information_child in information2.findall("language"):
            computer_language_name.append(information_child.get("name"))
            computer_language_name_count += 1
            computer_language_level.append(information_child.get("level"))
            for information_child2 in information_child.findall("period"):
                computer_language_value.append(information_child2.get("value"))
        computer_language_name_count_order.append(computer_language_name_count)
def summary():
    print("")
    print("< 요약 정보 >")
    print("* 전체 학생수 : %d명" %len(name))
    print("* 성별")
    print(" - 남학생 : %d명" %sex.count("남"))
    print(" - 여학생 : %d명" %sex.count("여"))
    print("* 전공여부")
    p = re.compile("^컴퓨터 공학|^통계")
    p_level = re.compile("상")
    p_python = re.compile("파이썬")
    major_count=0
    high_level_count=0
    python_experience_count=0
    for major_elements in major:
        if p.findall(major_elements): major_count +=1
        if p_level.findall(major_elements) : high_level_count +=1
        if p_python.findall(major_elements) : python_experience_count +=1
    print(" - 전공자(컴퓨터 공학, 통계): %d명(%d%%)"%(major_count, major_count/len(name)*100))
    print(" - 프로그래밍 언어 경험자 : %d명(%d%%)" %((len(name)-computer_language_name.count("None")), (len(name)-computer_language_name.count("None"))/len(name)*100))
    print(" - 프로그래밍 언어 상급자 : %d명" %high_level_count)
    print(" - 파이썬 경험자 : %d명" %python_experience_count)
    print("* 연령대")
    p_twenties = re.compile("[2].")
    p_thirties = re.compile("[3].")
    p_forties = re.compile("[4].")
    twenties=0
    thirties=0
    forties=0
    dic_name_age = {}
    for i in range(len(name)):
        dic_name_age[name[i]] = age[i]
    for i in name:
        if p_twenties.match(dic_name_age[i]):
            twenties +=1
        elif p_thirties.match(dic_name_age[i]):
            thirties +=1
        elif p_forties.match(dic_name_age[i]):
            forties +=1
    print(" - 20대 : %d명 (%d%%) [" %(twenties, twenties/len(name)*100), end=" ")
    for key, values in dic_name_age.items():
        if p_twenties.match(dic_name_age[key]):
            print(key, ":", values, end=" ")
    print("]\n - 30대 : %d명 (%d%%) [" %(thirties, thirties/len(name)*100), end=" ")
    for key, values in dic_name_age.items():
        if p_thirties.match(dic_name_age[key]):
            print(key, ":", values, end=" ")
    print("]\n - 40대 : %d명 (%d%%) [" %(forties, forties/len(name)*100), end=" ")
    for key, values in dic_name_age.items():
        if p_forties.match(dic_name_age[key]):
            print(key, ":", values, end=" ")
    print("]")

def all_information():
    print("")
    print("<전체 학생 데이터>")
    for count in range(len(name)):
        print("* "+name[count])
        print(" - 성별 : "+sex[count])
        print(" - 나이 : "+age[count])
        print(" - 전공 : "+major[count])
        print(" - 사용 가능한 컴퓨터 언어 : ",end=" ")
        for i in range(computer_language_name_count_order[count]):
            if computer_language_name[0] == 'None':
                print("없음",end=" ")
            else:
                print("\n  > "+computer_language_name[0]+" (학습기간 : "+computer_language_value[0]+", Level : "+computer_language_level[0]+")",end=" ")
            computer_language_level.pop(0)
            computer_language_value.pop(0)
            computer_language_name.pop(0)
        print("")

while True:
    print("")
    print("<화면출력>\n학생 정보 XML 데이터 분석 시작..\n\n1. 요약정보\n2. 전체 데이터 조회\n3. 종료")
    user_input = int(input("메뉴 입력 : "))
    if user_input == 1:
        summary()
    elif user_input == 2:
        all_information()
        print("")
    elif user_input == 3:
        print("프로그램을 종료합니다.")
        exit()

