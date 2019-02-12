def sum5(a,b): # sum2 로 변경
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("두 인자의 형이 다릅니다.")
        return
    else:
        result = sum5(a,b)
        return result

if __name__ == "__main__":
    print(sum5(1,2))
    print(safe_sum(1,2))
    print(safe_sum(1,"2"))