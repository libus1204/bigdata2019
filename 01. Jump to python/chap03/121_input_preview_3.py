# coding: cp949

age = input("���̸� �Է��ϼ��� : ")
if int(age)>=0 and int(age)<=3:
    print("���ϴ� ��� ����̸� ����� �����Դϴ�.")
elif int(age) >= 4 and int(age) <= 13:
    print("���ϴ� ��� ����̸� ����� 2000���Դϴ�.")
    pay = input("����� �Է��ϼ���. : ")
    if int(pay) > 2000:
        sub1 = int(pay)-2000
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %sub1)
    elif int(pay) < 2000:
        sub2 = 2000 - int(pay)
        print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %s����  ��ȯ�մϴ�." %(sub2,pay))
    else:print("�����մϴ�. Ƽ���� �����մϴ�.")
elif int(age) >= 14 and int(age) <= 18:
    print("���ϴ� û�ҳ� ����̸� ����� 3000���Դϴ�.")
    pay = input("����� �Է��ϼ���. : ")
    if int(pay) > 3000:
        sub1 = int(pay)-3000
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %sub1)
    elif int(pay) < 3000:
        sub2 = 3000 - int(pay)
        print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %s����  ��ȯ�մϴ�." %(sub2,pay))
    else:print("�����մϴ�. Ƽ���� �����մϴ�.")
elif int(age) >= 19 and int(age) <= 65:
    print("���ϴ� ���� ����̸� ����� 5000���Դϴ�.")
    pay = input("����� �Է��ϼ���. : ")
    if int(pay) > 5000:
        sub1 = int(pay)-5000
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�." %sub1)
    elif int(pay) < 5000:
        sub2 = 5000 - int(pay)
        print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %s����  ��ȯ�մϴ�." %(sub2,pay))
    else:print("�����մϴ�. Ƽ���� �����մϴ�.")
elif int(age) < 0:
    print("�ٽ� �Է��ϼ���")
    
else:print("���ϴ� ���� ����̸� ����� �����Դϴ�.")

