f=open("./learning_python.txt", 'r')
lines = f.readlines()
f.close()
f = open("./learning_python_copyed.txt", 'w') # 수정할 코드를 bbb 파일에 저장
for line in lines:
    f.write(line.replace("python", "C"))
f.close()
