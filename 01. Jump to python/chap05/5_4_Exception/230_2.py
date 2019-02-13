# try, except 이용

try:
    result = 4/0
    print(result)
except ZeroDivisionError:  # ZeroDivisionError 발생
    print("비정상 종료")  # 비정상 종료 멘트 출력

print("Program End")

