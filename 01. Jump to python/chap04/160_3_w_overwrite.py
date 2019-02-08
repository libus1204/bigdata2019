f=open("./file2.txt", 'w')
f.write("Hello World!!!!!!!!!!!!")
# 2번 라인 수행후 주석처리하고 재실행시 메세지는 Overwrite 된다.
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
f.close()