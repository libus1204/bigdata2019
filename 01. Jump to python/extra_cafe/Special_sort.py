user_input = input("정수 배열을 입력하세요(공백으로 구분) : ").split()
negative_number = []
positive_number = []
for i in range(len(user_input)):
    if int(user_input[i]) < 0:
        negative_number.append(user_input[i])
    else: positive_number.append(user_input[i])
total_list = negative_number + positive_number
for i in total_list:
    print(i, end=" ")


