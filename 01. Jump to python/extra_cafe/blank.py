f = open("./aaa.txt.", 'r') # 소스코드가 aaa 파일에 있다고 가정
lines = f.readlines()
f.close()
f = open("./bbb.txt", 'w') # 수정할 코드를 bbb 파일에 저장
for line in lines:
    f.write(line.replace("\t", "    "))
f.close()


