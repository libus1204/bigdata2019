# coding: cp949
count = 0
free = 3
year = 5
while True:
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
    else:
        print("���ϴ� %s ����̸� ����� %s �Դϴ�." %(level,pay))
        cate=int(input("��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ� ī��)"))
        if cate==1:
            fee=int(input("����� �Է��ϼ��� : "))
            if int(pay) < fee:
                count +=1
                sub=fee-int(pay)
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s ���� ��ȯ�մϴ�." %sub)
            elif int(pay) > fee:
                sub=int(pay)-fee
                print("%s ���� ���ڶ��ϴ�. �Է��Ͻ� %s ���� ��ȯ�մϴ�." %(sub,fee))
            else:
                count +=1
                print("�����մϴ�. Ƽ���� �����մϴ�.")
        else:
            count += 1
            credit = int(pay)*0.9
            if age >= 60 and age <= 65:
                credit = credit*0.95
            print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %credit)
        
        if not free == 0 and count%7 == 0 :
            free -= 1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %s��)" %(free))
        elif not year == 0 and count%4 == 0 :
            year -= 1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ���� Ƽ�� %s��" %(year)) 

    # modify1 ��������� �ڵ����� ����
