# coding: cp949

print("마름모 출력 프로그램 ver1.0\n")
while True:
    enter_num = int(input("홀수를 입력하세요(0 <- 종료): "))
    len_nemo = int((enter_num/2)+1)
    if enter_num == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    else:
        for i in range(1, len_nemo+1):
            print(" "*(len_nemo-i)+"*"*(2*i-1))
