user_input = str(input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : "))
user_restaurant = user_input.split(' ')
name = user_restaurant[0]
type = user_restaurant[1]

class MyRestaurant_ver_3:
    number_served = 0
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고, %s 전문점입니다." %(self.restaurant_name, self.cuisine_type))
    def open_restaurant(self):
        yes_or_no = input("레스토랑을 오픈하시겠습니까? (Y/N) : ")
        if yes_or_no == 'Y':
            print("저희 %s 레스토랑이 오픈했습니다." % self.restaurant_name)
        else:
            print("프로그램을 종료합니다.")
            exit()
    def reset_number_served(self, number):
        number = self.number_served = 0
        print("손님 카운팅을 0으로 초기화 하였습니다.")
        return self.number_served
    def increment_number_served(self, number):
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다." % number)
        self.number_served += int(number)
    def check_customer_number(self):
        print("지금까지 총 %s명 손님께서 오셨습니다." % self.number_served)
    def closed_restaurant(self):
        print("%s 레스토랑 문 닫습니다." %self.restaurant_name)
        exit()

ver3 = MyRestaurant_ver_3(name, type)
ver3.describe_restaurant()
ver3.open_restaurant()
while True:
    number = str(input("어서오세요. 몇 명 이십니까?(초기화:0, 입력, 종료:-1, 누적고객확인:p) : " ))
    if number == str(0):
        ver3.reset_number_served(number)
    elif number == str(-1):
        ver3.closed_restaurant()
    elif number == 'p':
        ver3.check_customer_number()
    else:
        ver3.increment_number_served(number)