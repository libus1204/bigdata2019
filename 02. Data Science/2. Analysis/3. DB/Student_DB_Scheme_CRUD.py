import MySQLdb, sys, csv

input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='student_info', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()
# CSV 파일 만들기
# data = ['Student_ID,Name,Sex,Age,Major,Languages,High_level,Middle_level,Low_level',
#         'ITT001,영호,남,45,경영학,,,,',
#         'ITT002,민선,여,25,컴퓨터 공학,C Java C++,,C,Java C++',
#         'ITT003,상민,남,30,전자 공학,C C++,,,C C++',
#         'ITT004,세중,남,30,정치외교,,,,',
#         'ITT005,규동,남,29,천문우주과학,Java Ruby,,Java,Ruby,',
#         'ITT006,치우,남,30,신문방송학,,,,',
#         'ITT007,현기,남,28,통계빅데이터,sas R,,sas,R',
#         'ITT008,정헌,남,30,전자 공학,C Verilog,,C,Verilog']
# f = open('Student_Info.csv', 'w')
# f.write('\n'.join(data))
# f.close()

# Create
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    student = []
    for column_index in range(len(header)):
        student.append(row[column_index])
    # print(student)
    c.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", student)
#

c.execute("SELECT * FROM Student")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)
# con.commit()
#