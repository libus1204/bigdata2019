import csv, MySQLdb, sys, sqlite3

input_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='my_supplies', user='open_source', passwd='1111')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)

file_reader = open(input_file, 'r')
