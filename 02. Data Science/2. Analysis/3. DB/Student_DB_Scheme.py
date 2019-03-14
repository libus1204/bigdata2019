import MySQLdb, sys, csv
# input_file = sys.argv[1]
con = MySQLdb.connect(host='localhost', port=3306, db='student_info', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()
# file_reader = csv.reader(open(input_file, 'r'), delimiter=',')

def main_menu():
    print("\n\n학생정보 XML 데이터 분석 시작..\n\n"
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

def name_and_age(age_list):
    print("[", end=" ")
    for list in age_list:
        print(list ,end=" ")
    print("]")

def menu_1():
    print("< 요약 정보 >")
    print(" * 전체 학생 수 : %s" % c.execute("select*from student"))
    print(" * 성별")
    c.execute("select sex from student")
    rows = c.fetchall()
    male_count = 0
    female_count = 0
    for row in rows:
        for column_index in range(len(row)):
            if str(row[column_index]) == '남': male_count += 1
            else: female_count += 1
    print(" - 남학생 : %s명 (%s%%)" % (male_count, male_count/len(rows)*100))
    print(" - 여학생 : %s명 (%s%%)" % (female_count, female_count/len(rows)*100))
    print(" * 전공여부")
    c.execute("select major from student")
    rows_major = c.fetchall()
    major_count = 0
    for row in rows_major:
        for column_index in range(len(row)):
            if "컴퓨터" in str(row[column_index]) or "통계" in str(row[column_index]):
                major_count += 1
    print(" - 전공자(컴퓨터 공학, 통계) : %s명 (%s%%)" % (major_count, major_count/len(rows_major)*100))
    c.execute("select language from student")
    rows_lang = c.fetchall()
    exp_count = 0
    for row in rows_lang:
        for column_index in range(len(row)):
            if str(row[column_index]): exp_count += 1
    print(" - 프로그래밍 언어 경험자 : %s명 (%s%%)" % (exp_count, exp_count/len(rows_lang)*100))
    c.execute("select high_level from student")
    rows_high = c.fetchall()
    high_level_count = 0
    for row in rows_high:
        for column_index in range(len(row)):
            if str(row[column_index]): high_level_count += 1
    print(" - 프로그래밍 언어 상급자 : %s명 (%s%%)" % (high_level_count, high_level_count/len(rows_lang)*100))
    c.execute("select name, age from student")
    rows_age = c.fetchall()
    age_20_count = 0
    age_30_count = 0
    age_40_count = 0
    age_20_name = []
    age_30_name = []
    age_40_name = []
    for row in rows_age:
        if int(row[1]) >= 20 and int(row[1]) < 30:
            age_20_count += 1
            age_20_name.append('%s : %s' %(str(row[0]), str(row[1])))
        elif int(row[1]) >= 30 and int(row[1]) < 40:
            age_30_count += 1
            age_30_name.append('%s : %s' %(str(row[0]), str(row[1])))
        elif int(row[1]) >= 40:
            age_40_count += 1
            age_40_name.append('%s : %s' %(str(row[0]), str(row[1])))
    print(" * 연령대")
    print(" - 20대 : %s명 (%s%%)" % (int(age_20_count), int(age_20_count)/len(rows)*100), end=" ")
    name_and_age(age_20_name)
    print(" - 30대 : %s명 (%s%%)" % (int(age_30_count), int(age_30_count)/len(rows)*100), end=" ")
    name_and_age(age_30_name)
    print(" - 40대 : %s명 (%s%%)" % (int(age_40_count), int(age_40_count)/len(rows)*100), end=" ")
    name_and_age(age_40_name)

def menu_2():
    while True:
        c.execute("select Student_ID from student")
        rows_itt = c.fetchall()
        input_data = []
        lang_name = []
        lang_high = []
        lang_mid = []
        lang_low = []
        for row in rows_itt:
            row_list_output = []
            for column_index in range(len(row)):
                row_list_output.append(str(row[column_index]))
        id_student = int(row_list_output[0][-3:]) + 1
        it_num = "ITT" + str(id_student).zfill(3)
        input_data.append(it_num)
        print("\n <신규 학생 정보 입력>")
        input_name = input(" - 이름을 입력하세요 (종료는 'Enter' 입력) : ")
        input_data.append(input_name)
        if not input_name: return
        input_sex = input(" - 성별을 입력하세요 : ")
        input_data.append(input_sex)
        input_age = input(" - 나이를 입력하세요 : ")
        input_data.append(int(input_age))
        input_major = input(" - 전공을 입력하세요 : ")
        input_data.append(input_major)
        print("사용 가능한 컴퓨터 언어를 입력하세요")
        while True:
            input_lang = input(" > 언어 이름(종료는 'Enter' 입력) : ")
            if not input_lang: break
            else:
                lang_name.append(input_lang)
                input_lang_level = input(" > 수준(상, 중, 하) : ")
                if input_lang_level == '상': lang_high.append(input_lang)
                elif input_lang_level == '중': lang_mid.append(input_lang)
                elif input_lang_level == '하':  lang_low.append(input_lang)

        c.execute("INSERT INTO student VALUES ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s');" % (it_num, input_name, input_sex,
                    int(input_age), input_major, ",".join(lang_name), ",".join(lang_high), ",".join(lang_mid),
                                                                               ",".join(lang_low)))
        # c.execute("SELECT * FROM Student")
        # rows = c.fetchall()
        # for row in rows:
        #     row_list_output = []
        #     for column_index in range(len(row)):
        #         row_list_output.append(str(row[column_index]))
        #     print(row_list_output)
        # con.commit()

def menu_3_main():
    print("\n<조회 서브 메뉴>\n1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴")
    menu3_input = input("메뉴 입력 : ")
    if menu3_input == '3': return
    elif menu3_input == '1':
        menu_3_1()
    elif menu3_input == '2':
        menu_3_2()

def menu_3_1():
    while True:
        c.execute('select * from student')
        rows = c.fetchall()
        print("\n< 검색 조건 >\n1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명"
              "\n6. 컴퓨터 언어 레벨\n7. 상위 메뉴")
        menu3_1_input = input("메뉴 입력 : ")
        if menu3_1_input == '8':
            break
            menu_3_main()
        menu3_search = input("검색어를 입력하세요 : ")
        stud_order = []
        if menu3_1_input == '1':
            for count in range(len(rows)):
                if str(rows[count][0]) == menu3_search:
                    stud_order.append(count)
        elif menu3_1_input == '2':
            for count2 in range(len(rows)):
                if menu3_search in str(rows[count2][1]):
                    stud_order.append(count2)
        elif menu3_1_input == '3':
            for count3 in range(len(rows)):
                if str(rows[count3][3]) == menu3_search:
                    stud_order.append(count3)
        elif menu3_1_input == '4':
            for count4 in range(len(rows)):
                if menu3_search in str(rows[count4][4]):
                    stud_order.append(count4)
        elif menu3_1_input == '5':
            for count5 in range(len(rows)):
                if menu3_search in str(rows[count5][5]):
                    stud_order.append(count5)
        elif menu3_1_input == '6':
            if menu3_search == '상':
                for count6 in range(len(rows)):
                    if rows[count6][6]:
                        stud_order.append(count6)
            if menu3_search == '중':
                for count7 in range(len(rows)):
                    if rows[count7][7]:
                        stud_order.append(count7)
            if menu3_search == '하':
                for count8 in range(len(rows)):
                    if rows[count8][8]:
                        stud_order.append(count8)

        if len(stud_order) == 1:
            new_stud = stud_order[0]
            print(" * %s (%s)" % (rows[new_stud][1], rows[new_stud][0]))
            print(" - 성별 : %s" % rows[new_stud][2])
            print(" - 전공 : %s" % rows[new_stud][4])
            print(" - 사용 가능한 언어")
            if not rows[new_stud][5]:
                print("  없음")
            else:
                if " " in rows[new_stud][6]:
                    rows[new_stud][6].split(' ')
                    for count in range(len(rows[new_stud][6].split(' '))):
                        print(" > %s (Level : 상)" % rows[new_stud][6].split(' ')[count])
                elif not rows[new_stud][6]:
                    pass
                else:
                    print(" > %s (Level : 상)" % rows[new_stud][6])
                if " " in rows[new_stud][7]:
                    rows[new_stud][7].split(' ')
                    for count in range(len(rows[new_stud][7].split(' '))):
                        print(" > %s (Level : 중)" % rows[new_stud][7].split(' ')[count])
                elif not rows[new_stud][7]:
                    pass
                else:
                    print(" > %s (Level : 중)" % rows[new_stud][7])
                if " " in rows[new_stud][8]:
                    rows[new_stud][8].split(' ')
                    for count in range(len(rows[new_stud][8].split(' '))):
                        print(" > %s (Level : 하)" % rows[new_stud][8].split(' ')[count])
                elif not rows[new_stud][8]:
                    pass
                else:
                    print(" > %s (Level : 하)" % rows[new_stud][8])
        elif len(stud_order) >= 2:
            for count in stud_order:
                print(" - %s (%s, %s, %s)" % (rows[count][0], rows[count][1], rows[count][3], rows[count][2]))

def menu_3_2():
    c.execute("select * from student")
    rows = c.fetchall()
    print("\n< 전체 학생 데이터 >")
    for student in range(len(rows)):
        print("\n* %s (%s)" % (rows[student][1], rows[student][0]))
        print(" - 성별 : %s" % rows[student][2])
        print(" - 나이 : %s" % rows[student][3])
        print(" - 전공 : %s" % rows[student][4])
        print(" - 사용 가능한 컴퓨터 언어 ")
        if not rows[student][5]: print(" > 없음")
        else:
            if " " in rows[student][6]:
                rows[student][6].split(' ')
                for count in range(len(rows[student][6].split(' '))):
                    print(" > %s (Level : 상)" % rows[student][6].split(' ')[count])
            elif not rows[student][6]:
                pass
            else:
                print(" > %s (Level : 상)" % rows[student][6])
            if " " in rows[student][7]:
                rows[student][7].split(' ')
                for count in range(len(rows[student][7].split(' '))):
                    print(" > %s (Level : 중)" % rows[student][7].split(' ')[count])
            elif not rows[student][7]:
                pass
            else:
                print(" > %s (Level : 중)" % rows[student][7])
            if " " in rows[student][8]:
                rows[student][8].split(' ')
                for count in range(len(rows[student][8].split(' '))):
                    print(" > %s (Level : 하)" % rows[student][8].split(' ')[count])
            elif not rows[student][8]:
                pass
            else:
                print(" > %s (Level : 하)" % rows[student][8])

def menu_4():
    c.execute("select * from student")
    rows = c.fetchall()
    print("수정할 학생의 ID를 입력하세요 : ",end='')
    update_id = input("")
    for count in range(len(rows)):
        if str(rows[count][0]) == update_id:
            print("\n1. 이름 : %s" % rows[count][1])
            print("2. 성별 : %s" % rows[count][2])
            print("3. 나이 : %s:" % rows[count][3])
            print(" - 전공 : %s" % rows[count][4])
            print("사용 가능한 언어")
            if not rows[count][5]:
                print("  없음")
            else:
                if " " in rows[count][6]:
                    rows[count][6].split(' ')
                    for count2 in range(len(rows[count][6].split(' '))):
                        print(" > %s (Level : 상)" % rows[count][6].split(' ')[count2])
                elif not rows[count][6]:
                    pass
                else:
                    print(" > %s (Level : 상)" % rows[count][6])
                if " " in rows[count][7]:
                    rows[count][7].split(' ')
                    for count2 in range(len(rows[count][7].split(' '))):
                        print(" > %s (Level : 중)" % rows[count][7].split(' ')[count2])
                elif not rows[count][7]:
                    pass
                else:
                    print(" > %s (Level : 중)" % rows[count][7])
                if " " in rows[count][8]:
                    rows[count][8].split(' ')
                    for count2 in range(len(rows[count][8].split(' '))):
                        print(" > %s (Level : 하)" % rows[count][8].split(' ')[count2])
                elif not rows[count][8]:
                    pass
                else:
                    print(" > %s (Level : 하)" % rows[count][8])

def menu_5():
    print("삭제할 ID를 입력하세요 : ",end="")
    user_delete = input("")
    c.execute("SELECT * FROM Student")
    rows = c.fetchall()
    c.execute("delete from student where student_id='%s'" % user_delete)
    print("삭제되었습니다.")
    # for row in rows:
    #     row_list_output = []
    #     for column_index in range(len(row)):
    #         row_list_output.append(str(row[column_index]))
    # print(row_list_output)




















































while True:
    main_menu()