# def search_visitor(name):
f = open("./방명록.txt", 'r', encoding='UTF-8')
lines = f.readlines()
name=str(input("이름을 입력하세요 : "))
guest_name=0
def search_visitor(name):
    global guest_name
    name_list=0
    for name_elements in lines:
        slice_elements=lines[name_list]
        guest_name=str(slice_elements[:3])
        name_list += 1
        if name == guest_name:
            print(guest_name+"님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
            return guest_name
        else: return ''
def guest_birthday():
    birthday = int(input("생년월일을 입력하세요 (예:801212): "))
    print("환영합니다!")
    save = guest_name+" "+birthday
    f.write(save)
    f.close()

search_visitor(name)
if guest_name == 0:
    guest_birthday()