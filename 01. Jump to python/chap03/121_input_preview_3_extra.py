# coding: cp949

age = int(input("���̸� �Է��ϼ��� : "))
if age >= 0 and age <= 3:
    level = "����"
    pay = "����"
elif age >=4 and age <= 13:
    level = "���"
    pay = "2000"
elif age >= 14 and age <= 18:
    level ="û�ҳ�"
    pay = "3000"
elif age >= 19 and age <= 65:
    level = "����"
    pay = "5000"
elif age < 0:
    print("�ٽ� �Է��ϼ���")
    exit()
else:
    level = "����"
    pay = "����"

if pay == "����":
    print("���ϴ� %s ����̸� ����� %s �Դϴ�." %(level,pay))
    exit()
else:
    print("���ϴ� %s ����̸� ����� %s �Դϴ�." %(level,pay))
    fee=int(input("����� �Է��ϼ��� : "))
    if int(pay) < fee:
        sub=fee-int(pay)
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s ���� ��ȯ�մϴ�." %sub)
    elif int(pay) > fee:
        sub=int(pay)-fee
        print("%d ���� ���ڶ��ϴ�. �Է��Ͻ� %d ���� ��ȯ�մϴ�." %(sub,fee))
    else: print("�����մϴ�. Ƽ���� �����մϴ�.")
