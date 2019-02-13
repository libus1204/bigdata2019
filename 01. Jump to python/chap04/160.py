# f=open("새파일.txt.txt", 'w') # 현재 소스코드 파일이 있는 경로에 파일 생성
                           # Unix(리눅스) 계열에서는 실행이 안 될 수도 있다.
# f=open("D:\새파일.txt.txt", 'w') # 절대경로(absolute path)에 파일 생성
# f=open("D:/새파일.txt.txt", 'w')
# f=open("D:\MyPath\새파일.txt.txt", 'w')
# f=open("D:/MyPath/새파일.txt.txt", 'w')
# f=open("D:\MyPath\new\새파일.txt.txt", 'w') # \n 이 특수문자 (줄바꿈) 이기 때문에 에러발생
# f=open("D:\MyPath\\new\새파일.txt.txt", 'w') # \\ 이 문자는 \ 로 인식
# f=open("D:\\MyPath\\new\\새파일.txt.txt", 'w') # 실수를 줄이기 위해서 경로를 표시할때는 모든 \를 \\로 표시한다.
f=open("D:/MyPath/new/새파일.txt.txt", 'w') # /를 한번만 사용해도 됨
# 하위 버전과 연동이 되는지는 확인해야 함
f.close()
