#coding: cp949

while True:
    input_odd = int(input("홀수를 입력하세요(0<-종료):"))
    
    if not input_odd:
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    mid_point = int(input_odd/2) 
    for i in range(0,input_odd):
        for j in range(0,input_odd):  
            if i<mid_point+1 and j>=mid_point-i and j<=mid_point+i:
                print("*",end='')
            elif i>mid_point and j>=i-mid_point and j<=input_odd-i+mid_point-1:
                print("*",end='')
            else:
                print(" ",end='')
        print("")

    
