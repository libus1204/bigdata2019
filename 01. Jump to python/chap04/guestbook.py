input_name=str(input("이름을 입력하세요 : "))
#
def search_visitor(input_name):
    guest_name = 0
    f = open("./방명록.txt", 'r', encoding='utf-8-sig')
    name_list= 0
    lines = f.readlines()
    list_lines=list(lines)
    print(list_lines)
    for name_elements in lines:
        slice_elements=lines[name_list]
        guest_name=slice_elements[:3]
        print(guest_name)
        name_list += 1
    if input_name == guest_name:
        print(guest_name+"님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
        return input_name
    else: return input_name = ''

def guest_birthday():
    f = open("./방명록.txt", 'a', encoding='utf-8-sig')
    birthday = str(input("생년월일을 입력하세요 (예:801212): "))
    print("환영합니다!")
    save = str(input_name)+" "+birthday+"\n"
    f.write(save)
    f.close()

search_visitor(input_name)
if not input_name:
    guest_birthday()