all_name="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
name_list=list(all_name.split(','))

# 1번
first_name_list=[]
len_name_list = int(len(name_list))
for i in range(len_name_list):
     first_name_list.append(name_list[i][0])
print(first_name_list.count("김"),"명 입니다.")
print(first_name_list.count("이"),"명 입니다.")

# 2번
print(name_list.count("이재영"),"명 반복됩니다.")

# 3번
set_name_list = set(name_list)
list_set_name_list = list(set_name_list)
for i in set_name_list:
     print(i, end=" ")
print("")
# 4번
list_set_name_list.sort()
for i in set_name_list:
     print(i, end=" ")
