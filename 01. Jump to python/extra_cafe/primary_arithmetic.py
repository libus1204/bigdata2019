carry_operation_list = []
while True:
    carry_operation = 0
    a, b = input("숫자 입력하세요 : ").split()
    if a == '0' and b == '0':
        break
    for count in range(len(a)):
        if int(a[count]) + int(b[count]) >= 10:
            carry_operation += 1
    carry_operation_list.append(carry_operation)
    print(carry_operation_list)
for carry_count in range(len(carry_operation_list)):
    if carry_operation_list[carry_count] == 0:
        print("None carry operation.")
    else: print("%s carry operation." % carry_operation_list[carry_count])



