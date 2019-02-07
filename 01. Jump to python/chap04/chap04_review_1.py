'''
# p.143
def sum(a,b):
    return a+b

d=3
e=4
c=sum(d,e)
print(c)
'''
'''
# p.144 일반적함수
def sum(a,b):
    result = a+b
    return result

a=sum(6,4)
print(a)
'''
'''
# p.144 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)
'''
'''
# p.145 결과값이 없는 함수
def sum(a,b):
    print("%d, %d 의 합은 %d 입니다." %(a, b, a+b))

sum(5,6)
'''
'''
# p.146 입력값도 결과값도 없는 함수
def say():
    print('Hi')

say()
'''

# p.147 여러 개의 입력값을 받는 함수 만들기
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "sub":
        result = 0
        for i in args:
            result -= i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "div":
        result = 1000
        for i in args:
            result /= i
    return result

a = sum_mul("sum", 1,2,3,4,5,6,7,8,9,10,11,12)
print(a)

result = sum_mul("sub", 1,2,3,4,5,6,7,8,9,10,11,12)
print(result)

result = sum_mul('mul', 1,2,3,4,5,6,7,8,9,10,11,12)
print(result)

result = sum_mul('div', 1,2,2,5,5)
print(result)

'''

# p.149 함수 결과값은 언제나 하나
def sum_and_mul(a,b):
    return a+b, a*b
result = sum_and_mul(3,4)
sum, mul = sum_and_mul(3,4)
print(result)
print(sum)
print(mul)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('헤헤')
say_nick('ㅎㅎ')
say_nick('바보')
'''
'''
# p.152 입력 인수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %s살 입니다." % old)
    if man: print("남자입니다.")
    else: print("여자입니다.")

say_myself("김상민", 30, True)
say_myself('김상민', 30)
say_myself('김상미', 30, False)
'''
'''
# p.154 함수 안에서 선언된 변수의 효력 범위
a = 3
def vartest(a):
    a += 1
    return a
print(a) # 전역변수가 3이니까 3출력
a = vartest(a)
print(a) # vartest 함수에서 +1 이 되고 return 됐으므로 4 출력

def vartest2():
    global a
    a *= 2

print(a)
vartest2()
print(a)
'''
'''
# p.157 input 사용
#number = input("숫자를 입력하세요 : ")
#print(number)
print("life" "is" "too short")
print("life "+"is "+"too short!")
print("life", "is", "too short", "!")
for i in range(10):
    print(i, end=' ')
'''
