class MyRestaurant_ver_2:
    def __init__(self, name, type):
        user_restaurant = name_list[count].split(' ')
        name = user_restaurant[0]
        type = user_restaurant[1]
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고, %s 전문점입니다." %(self.restaurant_name, self.cuisine_type))
        print("저희 %s 레스토랑이 오픈했습니다." % self.restaurant_name)
    def __del__(self):
        print("%s 레스토랑 문닫습니다." % self.restaurant_name)
name = 0
name_list = ['first','second','third']
for count in range(3):
    name_list[count] = str(input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : "))
    name_list[count] = MyRestaurant_ver_2(name, type)
    name_list[count].describe_restaurant()
print("\n저녁 10시가 되었습니다.\n")