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
    # elif user_input == 3:
    #     menu_3_main()
    # elif user_input == 4:
    #     menu_4()
    # elif user_input == 5:
    #     menu_5()

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
    c.execute("select Student_ID from student")
    rows_itt = c.fetchall()
    input_data = []
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
    input_age = input(" - 나이를 입력하세요 : ")
    input_major = input(" - 전공을 입력하세요 : ")
    print("사용 가능한 컴퓨터 언어를 입력하세요")
    while True:
        input_lang = input(" > 언어 이름(종료는 'Enter' 입력) : ")
        if not input_lang: return
        input_lang_period = input(" > 학습 기간(년/개월 단위) : ")
        input_lang_level = input("수준(상, 중, 하) : ")



































































while True:
    main_menu()