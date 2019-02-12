def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("두 인자의 형이 다릅니다.")
        return
    else:
        result = sum(a,b)
        return result

if __name__ == "__main__":
# entry point. 프로그램이 수행한 모듈 : __main__ 으로 셋팅
# 그렇지 않을 경우에는 현재 모듈명
# 테스트하고 싶은 코드를 실행할 때 이용
    print(sum(1,2))
    print(safe_sum(1,2))
    print(safe_sum(1,"2"))
