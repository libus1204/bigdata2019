# coding: cp949
count = 0
free = 3
year = 5
while True:
    age = int(input("나이를 입력하세요 : "))
    if age >= 0 and age <= 3:
        level = "유아"
        pay = "무료"
    elif age >=4 and age <= 13:
        level = "어린이"
        pay = "2000"
    elif age >= 14 and age <= 18:
        level ="청소년"
        pay = "3000"
    elif age >= 19 and age <= 65:
        level = "성인"
        pay = "5000"
    elif age < 0:
        print("다시 입력하세요")
        exit()
    else:
        level = "노인"
        pay = "무료"

    if pay == "무료":
        print("귀하는 %s 등급이며 요금은 %s 입니다." %(level,pay))
    else:
        print("귀하는 %s 등급이며 요금은 %s 입니다." %(level,pay))
        cate=int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)"))
        if cate==1:
            fee=int(input("요금을 입력하세요 : "))
            if int(pay) < fee:
                count +=1
                sub=fee-int(pay)
                print("감사합니다. 티켓을 발행하고 거스름돈 %s 원을 반환합니다." %sub)
            elif int(pay) > fee:
                sub=int(pay)-fee
                print("%s 원이 모자랍니다. 입력하신 %s 원을 반환합니다." %(sub,fee))
            else:
                count +=1
                print("감사합니다. 티켓을 발행합니다.")
        else:
            count += 1
            credit = int(pay)*0.9
            if age >= 60 and age <= 65:
                credit = credit*0.95
            print("%d원 결제 되었습니다. 티켓을 발행합니다." %credit)
        
        if not free == 0 and count%7 == 0 :
            free -= 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %s장)" %(free))
        elif not year == 0 and count%4 == 0 :
            year -= 1
            print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인 티켓 %s장" %(year)) 
