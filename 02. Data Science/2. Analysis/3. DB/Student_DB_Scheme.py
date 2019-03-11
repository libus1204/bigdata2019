import csv, MySQLdb, sys, sqlite3

input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='my_supplies', user='open_source', passwd='1111')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)

# user_name = input("사용자 이름을 입력하세요 : ")
# user_age = input('사용자 나이를 입력하세요 : ')
# user_major = input("사용자 전공을 입력하세요 : ")
# user_prac_lang = input("사용 가능한 언어를 입력하세요(콤마로 구분, 없을 경우 엔터) : ")
# if not user_prac_lang:
#     pass
# user_prac_level = input("사용 가능한 언어 수준을 입력하세요(위에 입력한 순서대로 입력, 콤마로 구분) : ")
# user_id =
# data = []
print(len(header))
#
# for row in file_reader:
#     data = []
#     for column_index in range(len(header)):
#         data.append(row[column_index])



