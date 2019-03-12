import MySQLdb, sys, csv

input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='student_info', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')

c.execute("select student_id from student")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)
print(row_list_output[0][-3:])