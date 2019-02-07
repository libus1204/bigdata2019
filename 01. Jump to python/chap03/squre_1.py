# coding: cp949

print("마름모 출력 프로그램 ver1.0\n")
while True:
    number = int(input("홀수를 입력하세요(0 <- 종료): "))
    number_integer = int((number/2)+1)
    if number == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    else:
        for i in range(1, number_integer+1):
            print(" "*(number_integer-i)+"*"*(2*i-1))
