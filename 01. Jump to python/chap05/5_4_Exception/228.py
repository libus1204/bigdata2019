print("progress 1")
f = open("새파일.txt", 'r') # 현재 디렉토리를 경로로 잡음
print("progress 2")
f.close()
print("progress 3") #  현재 디렉토리에 새파일이 있어서 progress 3 까지 실행
f = open("나없는파일.txt", 'r')  # 현재 디렉토리에 나없는파일이 없어서 밑에 라인은 실행안됨
print("progress 4")
f.close()
print("progress 5")
