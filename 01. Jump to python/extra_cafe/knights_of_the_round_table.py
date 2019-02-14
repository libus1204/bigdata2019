import math
f=open("./table_len.txt", 'r') # 삼각형 길이가 적힌 파일 table_len.txt 오픈
lines = f.readlines()
f.close()
for line in lines:
    a, b, c = line.split()
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a+b+c)/2
    before_sqrt = (s-a)*(s-b)*(s-c)/s
    r = math.sqrt(before_sqrt)
    f=open("./radius_of_the_table.txt",'a')  # 원 반지름 파일을 열어 추가로 작성
    round_table = """The radius of the round table is : """+"{0:0.3f}".format(r)+"\n"
    f.write(str(round_table))
    f.close()
