from xml.etree.ElementTree import parse

tree = parse("students_info.xml")
root = tree.getroot()
students_tag = root.findall('student')
students_count = len(root)
male_count = 0
female_count = 0
major_count = 0
exp_count = 0
high_level_count = 0
python_count = 0
age_20_count = 0
age_30_count = 0
age_40_count = 0
age_20_list = []
age_30_list = []
age_40_list = []
def name_and_age(age_list):
    print("[", end=" ")
    for list in age_list:
        list_in_name, list_in_age = list.split(' ')
        print(" %s : %s" % (list_in_name, list_in_age),end=" ")
    print(" ]")
while True:
    print("<화면 출력>\n학생정보 XML 데이터 분석 시작..\n\n1. 요약정보\n2. 전체 데이터 조회\n3. 종료")
    user_input = input("메뉴 입력 : ")
    if user_input == '1':
        for student in range(students_count):
            if students_tag[student].get('sex') == '남':
                male_count += 1
            elif students_tag[student].get('sex') == '여':
                female_count += 1
            if students_tag[student].findtext('major') == "컴퓨터 공학" or "통계" in students_tag[student].findtext('major'):
                major_count += 1
            if students_tag[student].find('practicable_computer_languages'):
                exp_count += 1
            if students_tag[student].find('practicable_computer_languages'):
                for languages in students_tag[student].findall('language'):
                    if languages.findtext('level') == "상":
                        high_level_count += 1
                    if languages.findtext('name') == "파이썬" or "python":
                        python_count += 1
            if int(students_tag[student].findtext('age')) >= 20 and int(students_tag[student].findtext('age')) < 30:
                age_20_count += 1
                age_20_list.append('%s %s' %(students_tag[student].get('name'), students_tag[student].findtext('age')))
            if int(students_tag[student].findtext('age')) >= 30 and int(students_tag[student].findtext('age')) < 40:
                age_30_count += 1
                age_30_list.append('%s %s' % (students_tag[student].get('name'), students_tag[student].findtext('age')))
            if int(students_tag[student].findtext('age')) >= 40 and int(students_tag[student].findtext('age')) < 50:
                age_40_count += 1
                age_40_list.append('%s %s' %(students_tag[student].get('name'), students_tag[student].findtext('age')))
            student += 1
        print("< 요약 정보 >")
        print("* 전체 학생수 : %s명" % students_count)
        print("* 성별")
        print(" - 남학생 : %s명 (%0.1f%%)" % (male_count, (male_count/students_count)*100))
        print(" - 여학생 : %s명 (%0.1f%%)" % (female_count, (female_count/students_count)*100))
        print("* 전공여부")
        print(" - 전공자(컴퓨터 공학, 통계) : %s명 (%0.1f%%)" % (major_count, (major_count/students_count)*100))
        print(" - 프로그래밍 언어 경험자 : %s명 (%0.1f%%)" % (exp_count, (exp_count/students_count)*100))
        print(" - 프로그래밍 언어 상급자 : %s명 (%0.1f%%)" % (high_level_count, (high_level_count/students_count)*100))
        print(" - 파이썬 경험자 : %s명 (%0.1f%%)" % (python_count, (python_count/students_count)*100))
        print("* 연령대")
        print(" - 20대 : %s명 (%0.1f%%) " % (age_20_count, (age_20_count/students_count)*100),end=" ")
        name_and_age(age_20_list)
        print(" - 30대 : %s명 (%0.1f%%) " % (age_30_count, (age_30_count/students_count)*100),end=" ")
        name_and_age(age_30_list)
        print(" - 40대 : %s명 (%0.1f%%) " % (age_40_count, (age_40_count/students_count)*100),end=" ")
        name_and_age(age_40_list)
    elif user_input == '2':
        print("\n< 전체 학생 데이터 >")
        for student in range(students_count):
            print("\n* %s" % students_tag[student].get('name'))
            print(" - 성별 : %s" % students_tag[student].get('sex'))
            print(" - 나이 : %s" % students_tag[student].findtext('age'))
            print(" - 전공 : %s" % students_tag[student].findtext('major'))
            print(" - 사용 가능한 컴퓨터 언어 : ", end=" ")
            if students_tag[student].find('practicable_computer_languages').text:
                for languages in students_tag[student].find('practicable_computer_languages').findall('language'):
                    for lang_value in languages.findall('period'):
                       print("\n  > %s (학습기간 : %s, Level : %s)" % (languages.get('name'), lang_value.get('value'),
                                                                languages.get('level')),end=" ")
            else: print("없음", end=" ")
            student += 1
        print("\n")
    elif user_input == '3':
        print('\n학생 정보 분석 완료!')
        exit()

