result1 = 0
result2 = 0
result3 = 0
def adder1(num):
    global result1
    print("%d 값을 입력 받았습니다." % num)
    result1 += num
    return result1
def adder2(num):
    global result2
    print("%d 값을 입력 받았습니다." % num)
    result2 += num
    return result2
def adder3(num):
    global result3
    print("%d 값을 입력 받았습니다." % num)
    result3 += num
    return result3

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))
print(adder3(3))
print(adder3(6))
# 기능이 추가