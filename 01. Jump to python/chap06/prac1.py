f=open("./learning_python.txt", 'r')
lines = f.readlines()
f.close()
for line in lines:
    print(line, end="")
print("")
f = open("./learning_python_copyed.txt", 'w') # 수정할 코드를 bbb 파일에 저장
for line in lines:
    replace_python = line.replace("python", "C")
    f.write(replace_python)
    print(replace_python,end="")
f.close()


