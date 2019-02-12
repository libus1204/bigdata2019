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

print(safe_sum('a',1)) # 더할수 있는 것이 아닙니다. None 출력
print(safe_sum(1,4)) # 5 출력
print(sum(10,10.4)) # 20.4 출력
# module_prac2_driver.py 에서 계속