import MySQLdb, sys, csv

input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='student_info', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
# while True:
#     c.execute("select Student_ID from student")
#     rows_itt = c.fetchall()
#     input_data = []
#     lang_name = []
#     lang_high = []
#     lang_mid = []
#     lang_low = []
#     for row in rows_itt:
#         row_list_output = []
#         for column_index in range(len(row)):
#             row_list_output.append(str(row[column_index]))
#     id_student = int(row_list_output[0][-3:]) + 1
#     it_num = "ITT" + str(id_student).zfill(3)
#     input_data.append(it_num)
#     print("\n <신규 학생 정보 입력>")
#     input_name = input(" - 이름을 입력하세요 (종료는 'Enter' 입력) : ")
#     input_data.append(input_name)
#     if not input_name: exit()
#     input_sex = input(" - 성별을 입력하세요 : ")
#     input_data.append(input_sex)
#     input_age = input(" - 나이를 입력하세요 : ")
#     input_data.append(int(input_age))
#     input_major = input(" - 전공을 입력하세요 : ")
#     input_data.append(input_major)
#     print("사용 가능한 컴퓨터 언어를 입력하세요")
#     while True:
#         input_lang = input(" > 언어 이름(종료는 'Enter' 입력) : ")
#         if not input_lang: break
#         else:
#             lang_name.append(input_lang)
#             input_lang_level = input("수준(상, 중, 하) : ")
#             if input_lang_level == '상': lang_high.append(input_lang)
#             elif input_lang_level == '중': lang_mid.append(input_lang)
#             elif input_lang_level == '하':  lang_low.append(input_lang)
#
#     c.execute("INSERT INTO student VALUES ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s');" % (it_num, input_name, input_sex,
#                 int(input_age), input_major, ",".join(lang_name), ",".join(lang_high), ",".join(lang_mid),
#                                                                            ",".join(lang_low)))
    # c.execute("SELECT * FROM Student")
    # rows = c.fetchall()
    # for row in rows:
    #     row_list_output = []
    #     for column_index in range(len(row)):
    #         row_list_output.append(str(row[column_index]))
    # con.commit()

c.execute("SELECT * FROM Student")
rows = c.fetchall()
row_list_output = []
for row in rows:
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
# print(len(rows[1][5]))
c.execute("select * from student")
rows = c.fetchall()
print("수정할 학생의 ID를 입력하세요 : ", end='')
update_id = input("")
for count in range(len(rows)):
    if str(rows[count][0]) == update_id:
        print("\n1. 이름 : %s" % rows[count][1])
        print("2. 성별 : %s" % rows[count][2])
        print("3. 나이 : %s" % rows[count][3])
        print("4. 전공 : %s" % rows[count][4])
        print("사용 가능한 언어")
        if not rows[count][5]:
            print(" - 없음")
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

































# c.execute("SELECT * FROM Student")
# rows = c.fetchall()
# for row in rows:
#     row_list_output = []
#     for column_index in range(len(row)):
#         row_list_output.append(str(row[column_index]))