# coding: cp949

print("������ ��� ���α׷� ver2.0\n")

while True:
    enter_num = int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))
    len_nemo = int((enter_num/2)+1)
    if enter_num == 0:
        print("\n������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break
    else:
        print(" "+"-"*enter_num+" ")
        for i in range(1, len_nemo+1):
            print("|"+" "*(len_nemo-i)+"*"*(2*i-1)+" "*(len_nemo-i)+"|")
            if i == len_nemo:
                for i in range(1,len_nemo):
                    print("|"+" "*i+"*"*(enter_num-2*i)+" "*i+"|")
                    
        print(" "+"-"*enter_num+" ")

