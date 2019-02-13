# try, except as 이용

try:
    result = 4/0  # 0으로 나눌수가 없으므로 에러 발생
    print(result)
except ZeroDivisionError as e:  # Zero division error 발생 오류를 e 오류메시지 변수에 넣고
    print(e)  # e 출력
print("Program End")



# result = system_cal()
#
# if result == -1:
#     print(" xxxx 에러를 발생했습니다.")
#     exit()
# else:
#     print(result)
#
# print("Program End")
