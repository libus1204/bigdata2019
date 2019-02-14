user_input = input("숫자를 입력해주세요(공백으로 구분) : ").split()
check_number_count = 0
for number in user_input:
    a = number
    for number2 in range(0, 10):
        count = a.count(str(number2))
        if count != 1:
            check_number_count += 0
        else: check_number_count += 1
    if check_number_count != 10:
        print("False",end=" ")
        check_number_count = 0
    else: print("True", end=" ")

