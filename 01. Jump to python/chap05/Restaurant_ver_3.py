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
        open_or_close = input("레스토랑이 오픈하시겠습니까? (Y/n): " % self.restaurant_name)
        if open_or_close == "y":
            print("저희 %s 레스토랑이 오픈했습니다." % self.restaurant_name)
    def reset_number_served(self, number):
        self.number = 0
        print("손님 카운팅을 0으로 초기화 하였습니다.")
    def increment_number_served(self, number):
        print("손님 %s 명 들어오셨습니다. 자리를 안내해 드리겠습니다." % number)
        number += self.number_served
        return number
    def check_customer_number(self):
        print("지금까지 %s 명 손님께서 오셨습니다." %number)



ver3 = MyRestaurant_ver_3(name, type)
ver3.describe_restaurant()
ver3.open_restaurant()