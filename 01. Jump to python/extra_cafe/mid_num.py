user_number = input("3개의 숫자를 입력하세요 : ").split()
user_number = [int(i) for i in user_number]
user_number.sort()
print(user_number[1])