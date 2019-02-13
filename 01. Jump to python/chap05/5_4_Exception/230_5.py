try:  # 사람들이 많이 하는 style
    result = 4/2
    print(result)
    f = open("NA.txt", 'r')
    f.close()
except Exception as e:
    # 모든 Failure 를 동일하게 처리하고 싶고 Exception의 유형을 정확히 모를 때
    # 유용하다. (일반적인 상황에서 적용할 수 있는 Tip)
    print(e)

print("Program End")

# 위 코드가 밑 코드를 개선한 것
# result = system_cal()
#
# if result == -1:
#     print(" xxxx 에러를 발생했습니다.")
#     exit()
# else:
#     print(result)
#
# result = system_utill()
#
# if result == -1:
#     print(" xxxx 에러를 발생했습니다.")
#     exit()
# else:
#     print(result)
#
# print("Program End")