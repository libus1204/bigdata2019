#coding: cp949

while True:
    input_odd = int(input("Ȧ���� �Է��ϼ���(0<-����):"))
    
    if not input_odd:
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
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

    
