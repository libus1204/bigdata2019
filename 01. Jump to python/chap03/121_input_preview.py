# coding: cp949

age = input("나이를 입력하세요 : ")
if int(age)>=0 and int(age)<=3 or int(age)>=66:
    print("요금은 무료입니다.")
elif int(age) >= 4 and int(age) <= 13:
    print("요금은 2000원입니다.")
elif int(age) >= 14 and int(age) <= 18:
    print("요금은 3000원입니다.")
else: 
    print("요금은 5000원입니다.")
