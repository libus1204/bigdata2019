# coding: cp949

age = input("나이를 입력하세요 : ")
if int(age)>=0 and int(age)<=3:
    print("귀하는 어린이 등급이며 요금은 무료입니다.")
elif int(age) >= 4 and int(age) <= 13:
    print("귀하는 어린이 등급이며 요금은 2000원입니다.")
    cate = input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용카드)")
    if int(cate)==1:
        pay = input("요금을 입력하세요. : ")
        if int(pay) > 2000:
            sub1 = int(pay)-2000
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %sub1)
        elif int(pay) < 2000:
            sub2 = 2000 - int(pay)
            print("%d원이 모자랍니다. 입력하신 %s원을  반환합니다." %(sub2,pay))
        else:print("감사합니다. 티켓을 발행합니다.")
    else:
        credit = 2000*0.9
        print("%d원 결제되었습니다. 티켓을 발행합니다." %credit)
elif int(age) >= 14 and int(age) <= 18:
    print("귀하는 어린이 등급이며 요금은 3000원입니다.")
    cate = input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용카드)")
    if int(cate)==1:
        pay = input("요금을 입력하세요. : ")
        if int(pay) > 3000:
            sub1 = int(pay)-3000
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %sub1)
        elif int(pay) < 3000:
            sub2 = 3000 - int(pay)
            print("%d원이 모자랍니다. 입력하신 %s원을  반환합니다." %(sub2,pay))
        else:print("감사합니다. 티켓을 발행합니다.")
    else:
        credit = 3000*0.9
        print("%d원 결제되었습니다. 티켓을 발행합니다." %credit)
elif int(age) >= 19 and int(age) <= 65:
    print("귀하는 어린이 등급이며 요금은 5000원입니다.")
    cate = input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용카드)")
    if int(cate)==1:
        pay = input("요금을 입력하세요. : ")
        if int(pay) > 5000:
            sub1 = int(pay)-5000
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %sub1)
        elif int(pay) < 5000:
            sub2 = 5000 - int(pay)
            print("%d원이 모자랍니다. 입력하신 %s원을  반환합니다." %(sub2,pay))
        else:print("감사합니다. 티켓을 발행합니다.")
    else:
        credit = 5000*0.9
        if int(age)>=60 and int(age)<=65:
            credit2 = credit*0.95
            print("%d원 결제되었습니다. 티켓을 발행합니다." %credit2)
        else:
            print("%d원 결제되었습니다. 티켓을 발행합니다." %credit)
elif int(age) < 0:
    print("다시 입력하세요")

else: print("귀하는 노인 등급이며 요금은 무료입니다.")

