class MyRestaurant_ver_2:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고, %s 전문점입니다." %(self.restaurant_name, self.cuisine_type))
        print("저희 %s 레스토랑이 오픈했습니다." % self.restaurant_name)
    def __del__(self):
        print("%s 레스토랑 문닫습니다." % self.restaurant_name)

restaurant=[]
for count in range(3):
    user_input = str(input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : "))
    user_restaurant = user_input.split(' ')
    name = user_restaurant[0]
    type = user_restaurant[1]
    # restaurant.append(count)
    # restaurant[count] = MyRestaurant_ver_2(name, type)
    # restaurant[count].describe_restaurant()
    restaurant.append(MyRestaurant_ver_2(name, type))
    restaurant[count].describe_restaurant()
    print(restaurant)
print("\n저녁 10시가 되었습니다.\n")