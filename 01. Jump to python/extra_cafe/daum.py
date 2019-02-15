user_list = input("점을 만들 숫자를 입력하세요.(공백으로 구분) : ").split()
user_list_int = [int(i) for i in user_list]
closest_distance = 1
for order in range(0, len(user_list)-1):
    distance = user_list_int[order+1] - user_list_int[order]
    if closest_distance >= distance :
        closest_distance = distance
        closest_two_dot1 = user_list_int[order]
        closest_two_dot2 = user_list_int[order+1]
    else: pass
print(closest_two_dot1, closest_two_dot2)
