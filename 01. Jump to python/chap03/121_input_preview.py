# coding: cp949

age = input("���̸� �Է��ϼ��� : ")
if int(age)>=0 and int(age)<=3 or int(age)>=66:
    print("����� �����Դϴ�.")
elif int(age) >= 4 and int(age) <= 13:
    print("����� 2000���Դϴ�.")
elif int(age) >= 14 and int(age) <= 18:
    print("����� 3000���Դϴ�.")
else: 
    print("����� 5000���Դϴ�.")
