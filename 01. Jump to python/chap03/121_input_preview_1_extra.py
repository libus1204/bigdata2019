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

print("요금은 %s 입니다." %(pay))

