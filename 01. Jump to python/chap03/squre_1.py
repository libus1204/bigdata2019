# coding: cp949

print("������ ��� ���α׷� ver1.0\n")
while True:
    number = int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))
    number_integer = int((number/2)+1)
    if number == 0:
        print("\n������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break
    else:
        for i in range(1, number_integer+1):
            print(" "*(number_integer-i)+"*"*(2*i-1))
