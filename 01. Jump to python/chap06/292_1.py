user_input = input("압축할 문자열을 입력해주세요 : ")
string = user_input[0]
count = 0
for num in user_input:
    if num == string[-1]:
        count += 1
    else:
        string += str(count) + num
        count = 1
string += str(count)
print(string)
