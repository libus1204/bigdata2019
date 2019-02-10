name = str(input("이름을 입력하세요 : "))
def search_visitor(name):
    f=open("./방명록.txt", 'r', encoding='UTF-8-SIG')
    visitor = f.readlines()
    list_visitor_name = []
    for already_visitor in visitor:
        slice_name = already_visitor[:3]
        list_visitor_name.append(slice_name)
    if not name in list_visitor_name:
        return name
    else: return ''
    f.close()
def write_down_visitor(name):
    if search_visitor(name) == '':
        print(name+"님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요")
    else:
        birthday = int(input("생년월일을 입력하세요 : "))
        new_visitor = "\n"+name+" "+str(birthday)
        print(name+"님 환영합니다. 아래 내용을 입력하셨습니다.", end="")
        print(new_visitor)
        f=open("./방명록.txt", 'a', encoding='UTF-8-SIG')
        f.write(new_visitor)
        f.close()
search_visitor(name)
write_down_visitor(name)