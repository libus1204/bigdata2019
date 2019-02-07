# coding: cp949

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
    exit()
else:
    print("귀하는 %s 등급이며 요금은 %s 입니다." %(level,pay))
    fee=int(input("요금을 입력하세요 : "))
    if int(pay) < fee:
        sub=fee-int(pay)
        print("감사합니다. 티켓을 발행하고 거스름돈 %s 원을 반환합니다." %sub)
    elif int(pay) > fee:
        sub=int(pay)-fee
        print("%d 원이 모자랍니다. 입력하신 %d 원을 반환합니다." %(sub,fee))
    else: print("감사합니다. 티켓을 발행합니다.")
