# module_prac1 이라는 함수 파일 생성
def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a,b)
        return result

def mul(a,b):
    return a*b