# coding: cp949

print("마름모 출력 프로그램 ver2.0\n")
while True:
    num = int(input("홀수를 입력하세요(0 <- 종료): "))
    num2 = int((num/2)+1)
    if num == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    for i in range(1, num2+1):
        print(" "*(num2-i)+"*"*(2*i-1))
        if i == num2:
            for i in range(1,num2):
                print(" "*i+"*"*(num-2*i))

