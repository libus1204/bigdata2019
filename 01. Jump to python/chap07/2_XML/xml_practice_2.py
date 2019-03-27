from xml.etree.ElementTree import parse, ElementTree, SubElement
tree = parse("students_info_2.xml")
root = tree.getroot()
students_tag = root.findall('student')
students_count = len(root)
def name_and_age(age_list):
    print("[", end=" ")
    for list in age_list:
        list_in_name, list_in_age = list.split(' ')
        print(" %s : %s" % (list_in_name, list_in_age),end=" ")
    print(" ]")
def main_menu():
    print("\n\n<화면 출력>\n학생정보 XML 데이터 분석 시작..\n\n"
          "1. 요약정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료")
    user_input = int(input("메뉴 입력 : "))
    if user_input == 1:
        menu_1()
    elif user_input == 6:
        print("\n학생 정보 분석 완료!")
        exit()
    elif user_input == 2:
        menu_2()
    elif user_input == 3:
        menu_3_main()
    elif user_input == 4:
        menu_4()
    elif user_input == 5:
        menu_5()
def menu_1():
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
            age_20_list.append('%s %s' % (students_tag[student].get('name'), students_tag[student].findtext('age')))
        if int(students_tag[student].findtext('age')) >= 30 and int(students_tag[student].findtext('age')) < 40:
            age_30_count += 1
            age_30_list.append('%s %s' % (students_tag[student].get('name'), students_tag[student].findtext('age')))
        if int(students_tag[student].findtext('age')) >= 40 and int(students_tag[student].findtext('age')) < 50:
            age_40_count += 1
            age_40_list.append('%s %s' % (students_tag[student].get('name'), students_tag[student].findtext('age')))
        student += 1
    print("< 요약 정보 >")
    print("* 전체 학생수 : %s명" % students_count)
    print("* 성별")
    print(" - 남학생 : %s명 (%0.1f%%)" % (male_count, (male_count / students_count) * 100))
    print(" - 여학생 : %s명 (%0.1f%%)" % (female_count, (female_count / students_count) * 100))
    print("* 전공여부")
    print(" - 전공자(컴퓨터 공학, 통계) : %s명 (%0.1f%%)" % (major_count, (major_count / students_count) * 100))
    print(" - 프로그래밍 언어 경험자 : %s명 (%0.1f%%)" % (exp_count, (exp_count / students_count) * 100))
    print(" - 프로그래밍 언어 상급자 : %s명 (%0.1f%%)" % (high_level_count, (high_level_count / students_count) * 100))
    print(" - 파이썬 경험자 : %s명 (%0.1f%%)" % (python_count, (python_count / students_count) * 100))
    print("* 연령대")
    print(" - 20대 : %s명 (%0.1f%%) " % (age_20_count, (age_20_count / students_count) * 100), end=" ")
    name_and_age(age_20_list)
    print(" - 30대 : %s명 (%0.1f%%) " % (age_30_count, (age_30_count / students_count) * 100), end=" ")
    name_and_age(age_30_list)
    print(" - 40대 : %s명 (%0.1f%%) " % (age_40_count, (age_40_count / students_count) * 100), end=" ")
    name_and_age(age_40_list)
def menu_2():
    tree = parse("students_info_2.xml")
    root = tree.getroot()
    students_tag = root.findall('student')
    students_count = len(root)
    print("<신규 학생 정보 입력>")
    while True:
        new_name = input("- 이름을 입력하세요.(종료는 'Enter' 입력) : ")
        if not new_name:
            break
            main_menu()
        else:
            new_sex = input("- 성별을 입력하세요 : ")
            new_age = input("- 나이를 입력하세요 : ")
            new_major = input("- 전공을 입력하세요 : ")
            print("- 사용 가능한 컴퓨터 언어를 입력하세요 : ")
            new_lang = input(" > 언어 이름(종료는 'Enter' 입력) : ")
            if not new_lang :

                id_student = int(str(students_tag[-1].get("ID"))[3:])+1
                it_num = "ITT" + str(id_student).zfill(3)

                a = SubElement(root, "student", ID=it_num, name=new_name, sex=new_sex)
                SubElement(a, "age").text = new_age
                SubElement(a, "major").text = new_major
                SubElement(a, "practicable_computer_languages")
                ElementTree(root).write("students_info_2.xml",
                                        encoding="utf-8", xml_declaration=True)
            else:
                new_period = input(" > 학습 기간(년/개월 단위) : ")
                new_level = input(" > 수준(상, 중, 하) : ")
                menu_2_input_data(new_name, new_sex, new_age, new_major, new_lang, new_period, new_level)
def menu_2_input_data(new_stu_name, new_stu_sex, new_stu_age, new_stu_major, new_stu_lang, new_stu_period, new_stu_level):
    tree = parse("students_info_2.xml")
    root = tree.getroot()
    students_tag = root.findall('student')
    students_count = len(root)
    id_student = int(str(students_tag[-1].get("ID"))[3:]) + 1
    it_num = "ITT" + str(id_student).zfill(3)
    a = SubElement(root, "student", ID=it_num, name=new_stu_name, sex=new_stu_sex)
    SubElement(a, "age").text=new_stu_age
    SubElement(a, "major").text=new_stu_major
    b = SubElement(a, "practicable_computer_languages")
    c = SubElement(b, "language", level=new_stu_level, name=new_stu_lang)
    SubElement(c, "period", value = new_stu_period)
    ElementTree(root).write("students_info_2.xml", encoding="utf-8", xml_declaration=True)
def menu_3_main():
    print("<조회 서브 메뉴>\n1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴")
    user_menu3_input = input("메뉴 입력 : ")
    if user_menu3_input == '1':
        menu_3_1()
    if user_menu3_input == '2':
        menu_3_2()
    if user_menu3_input == '3':
        main_menu()
def menu_3_1():
    while True:
        print("\n1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간\n7. 컴퓨터 언어 레벨\n8. 상위 메뉴")
        user_menu_3_1_input = input("메뉴 입력 : ")
        students_order = []
        if user_menu_3_1_input == '8':
            break
            menu_3_main()
        user_menu_3_1_search = input("검색어를 입력하세요 : ")
        if user_menu_3_1_input == '1':
            for student in range(students_count):
                if students_tag[student].get('ID') == user_menu_3_1_search:
                    students_order.append(student)
        elif user_menu_3_1_input == '2':
            for student in range(students_count):
                if user_menu_3_1_search in students_tag[student].get('name'):
                    students_order.append(student)
        elif user_menu_3_1_input == '3':
            for student in range(students_count):
                if students_tag[student].findtext('age') == user_menu_3_1_search:
                    students_order.append(student)
        elif user_menu_3_1_input == '4':
            for student in range(students_count):
                if user_menu_3_1_search in students_tag[student].findtext('major'):
                    students_order.append(student)
        elif user_menu_3_1_input == '5':
            for student in range(students_count):
                if students_tag[student].find('practicable_computer_languages').text:
                    for languages in students_tag[student].find('practicable_computer_languages').findall('language'):
                        if languages.get('name') == user_menu_3_1_search:
                            students_order.append(student)
        elif user_menu_3_1_input == '6':
            for student in range(students_count):
                if students_tag[student].find('practicable_computer_languages').text:
                    for languages in students_tag[student].find('practicable_computer_languages').findall('language'):
                        for lang_value in languages.findall('period'):
                            if user_menu_3_1_search in lang_value.get('value'):
                                students_order.append(student)
        elif user_menu_3_1_input == '7':
            for student in range(students_count):
                if students_tag[student].find('practicable_computer_languages').text:
                    for languages in students_tag[student].find('practicable_computer_languages').findall('language'):
                        if languages.get('level') == user_menu_3_1_search:
                            students_order.append(student)
                            set1 = set(students_order)
                            students_order = list(set1)
        if len(students_order) == 1:
            student = students_order[0]
            print("\n* %s" % students_tag[student].get('name'),end= " ")
            print("(%s)" % students_tag[student].get('ID'))
            print(" - 성별 : %s" % students_tag[student].get('sex'))
            print(" - 나이 : %s" % students_tag[student].findtext('age'))
            print(" - 전공 : %s" % students_tag[student].findtext('major'))
            print(" - 사용 가능한 컴퓨터 언어 : ", end=" ")
            if students_tag[student].find('practicable_computer_languages').text:
                for languages in students_tag[student].find('practicable_computer_languages').findall('language'):
                    for lang_value in languages.findall('period'):
                        print("\n  > %s (학습기간 : %s, Level : %s)" % (languages.get('name'), lang_value.get('value'),
                                                                    languages.get('level')), end=" ")
            else: print("없음", end=" ")
            print("")
        if len(students_order) >= 2:
            for i in range(len(students_order)):
                student = students_order[i]
                print("\n- %s (%s, %s, %s)" % (students_tag[student].get('name'), students_tag[student].get('ID'),
                                               students_tag[student].findtext('age'), students_tag[student].get('sex')), end=" ")
            print("")
def menu_3_2():
    from xml.etree.ElementTree import parse
    tree = parse("students_info_2.xml")
    root = tree.getroot()
    students_tag = root.findall('student')
    students_count = len(root)
    print("\n< 전체 학생 데이터 >")
    for student in range(students_count):
        print("\n* %s" % students_tag[student].get('name'))
        print(" - 성별 : %s" % students_tag[student].get('sex'))
        print(" - 나이 : %s" % students_tag[student].findtext('age'))
        print(" - 전공 : %s" % students_tag[student].findtext('major'))
        print(" - 사용 가능한 컴퓨터 언어 : ", end=" ")
        if students_tag[student].find('practicable_computer_languages'):
            for languages in students_tag[student].find('practicable_computer_languages').findall('language'):
                for lang_value in languages.findall('period'):
                    print("\n  > %s (학습기간 : %s, Level : %s)" % (languages.get('name'), lang_value.get('value'),
                                                                languages.get('level')), end=" ")
        else:
            print("없음", end=" ")
def menu_4():
    languages_count = 5
    user_insert_num = input("수정할 학생의 ID를 입력하세요(엔터시 메인메뉴로 이동) :")
    if not user_insert_num:
        main_menu()
    for student in range(students_count):
        if students_tag[student].get('ID') == user_insert_num:
            student_insert = student
    # for student_insert in range(students_count):
    print("1. 이름 : %s" % students_tag[student_insert].get("name"))
    print("2. 성별 : %s" % students_tag[student_insert].get("sex"))
    print("3. 나이 : %s" % students_tag[student_insert].findtext("age"))
    print("4. 전공 : %s" % students_tag[student_insert].findtext('major'))
    print("사용 가능한 언어",end=" ")
    if students_tag[student_insert].find('practicable_computer_languages').text:
        for languages in students_tag[student_insert].find('practicable_computer_languages').findall('language'):
            for lang_value in languages.findall('period'):
                print("%s. %s" % (languages_count, languages.get('name')))
                print("%s. 학습기간 : %s" % (languages_count + 1, lang_value.get('value')))
                print("%s. Level : %s" % (languages_count + 2, languages.get('level')))
                languages_count += 3
    else: print("없음. 추가하시려면 숫자 '5'를 누르세요.")
    insert_num = int(input("\n수정할 항목의 번호를 입력하세요 : "))
    if not students_tag[student_insert].find('practicable_computer_languages').text and insert_num == 5:
        while True:
            modify_lang_name = input("추가하실 언어를 입력하세요(엔터 시 종료): ")
            if not modify_lang_name:
                break
                main_menu()
            modify_period = input("추가하실 기간을 입력하세요 : ")
            modify_level = input("추가하실 레벨을 입력하세요 : ")
            b = students_tag[student_insert][2]
            c = SubElement(b, "language", level=modify_level, name=modify_lang_name)
            SubElement(c, "period", value=modify_period)
            ElementTree(root).write("students_info_2.xml", encoding="utf-8", xml_declaration=True)
        print("\n* %s" % students_tag[student_insert].get('name'))
        print(" - 성별 : %s" % students_tag[student_insert].get('sex'))
        print(" - 나이 : %s" % students_tag[student_insert].findtext('age'))
        print(" - 전공 : %s" % students_tag[student_insert].findtext('major'))
        print(" - 사용 가능한 컴퓨터 언어 : ", end=" ")
        if students_tag[student_insert].find('practicable_computer_languages'):
            for languages in students_tag[student_insert].find('practicable_computer_languages').findall('language'):
                for lang_value in languages.findall('period'):
                    print("\n  > %s (학습기간 : %s, Level : %s)" % (languages.get('name'), lang_value.get('value'),
                                                                languages.get('level')), end=" ")
        main_menu()
    insert_contents = input("수정할 값을 입력하세요 : ")
    if insert_num == 3:
        students_tag[student_insert][0].text = insert_contents
    if insert_num == 4:
        students_tag[student_insert][0].text = insert_contents
    if insert_num >= 5:
            sum_lang = students_tag[student_insert].find('practicable_computer_languages').findall('language')
            cal = (insert_num-5)//3
            if insert_num % 3 == 2:
                sum_lang[cal].set("name", insert_contents)
            elif insert_num % 3 == 0:
                sum_lang[cal].find('period').set("value", insert_contents)
            elif insert_num % 3 == 1:
                sum_lang[cal].set("level", insert_contents)
    ElementTree(root).write("students_info_2.xml", encoding="utf-8", xml_declaration=True)
    print("\n* %s" % students_tag[student_insert].get('name'))
    print(" - 성별 : %s" % students_tag[student_insert].get('sex'))
    print(" - 나이 : %s" % students_tag[student_insert].findtext('age'))
    print(" - 전공 : %s" % students_tag[student_insert].findtext('major'))
    print(" - 사용 가능한 컴퓨터 언어 : ", end=" ")
    if students_tag[student_insert].find('practicable_computer_languages'):
        for languages in students_tag[student_insert].find('practicable_computer_languages').findall('language'):
            for lang_value in languages.findall('period'):
                print("\n  > %s (학습기간 : %s, Level : %s)" % (languages.get('name'), lang_value.get('value'),
                                                            languages.get('level')), end=" ")
def menu_5():
    user_delete = input("삭제할 ID를 입력하세요 : ")
    for student in range(students_count):
        if students_tag[student].get('ID') == user_delete:
            delete_id = student
    root.remove(students_tag[delete_id])
    ElementTree(root).write("students_info_2.xml", encoding="utf-8", xml_declaration=True)

while True:
    main_menu()
