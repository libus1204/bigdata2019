# coding: cp949

print("������ ��� ���α׷� ver2.0\n")
while True:
    num = int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))
    num2 = int((num/2)+1)
    if num == 0:
        print("\n������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break
    for i in range(1, num2+1):
        print(" "*(num2-i)+"*"*(2*i-1))
        if i == num2:
            for i in range(1,num2):
                print(" "*i+"*"*(num-2*i))

