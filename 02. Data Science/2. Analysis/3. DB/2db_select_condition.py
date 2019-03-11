import csv, sqlite3, sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
# 전체 레코드 조회 readlines() 와 유사
# output = c.execute("SELECT * FROM Suppliers")

# 열 필터링 하는 조건
# SQL 문은 대소문자를 구분하지 않는다. 그렇지만 성능을 위해
# SQL 문 필드, 테이블 명은 일관된 대소문자 정책을 적용해야 한다.
# output = c.execute("SELECT Suppliers_Name FROM Suppliers")
# output = c.execute("SELECT Suppliers_Name, Cost FROM Suppliers")
# output = c.execute("SELECT suppliers_name, cost FROM Suppliers")
# output = c.execute("SELECT suppliers_name, cost FROM Suppliers")
# output = c.execute("SELECT suppliers_name, cost FROM suppliers")

# 행 필터링 조건
# output = c.execute("SELECT * FROM suppliers WHERE supplier_name='Supplier X'")
# output = c.execute("SELECT * FROM suppliers WHERE cost > 300")

# 행, 열 필터링 하는 조건
output = c.execute("SELECT supplier_name, cost FROM Suppliers WHERE supplier_name = 'Supplier X'")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)