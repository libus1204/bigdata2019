try :  # 선생님 추천
    result = 4/0
    print(result)  # 분모가 0이 아닐 때 result 값 출력
except Exception as e:  # 분모가 0 이므로 e 출력
    print(e)

print("Program End")