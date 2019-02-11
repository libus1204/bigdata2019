class HousePark:
    __last_name__ = "박"
    def __init__(self, name):
        self.full_name = self.__last_name__ + name
    def travel(self, where):
        print("%s, %s 여행을 가다." %(self.full_name,where))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네" %(self.full_name, other.full_name))
    def fight(self,other):
        print("%s, %s 싸우네" %(self.full_name, other.full_name))
    def __add__(self, other):
        print("%s, %s 결혼했네" %(self.full_name, other.full_name))
    def __sub__(self, other):
        print("%s, %s 이혼했네" %(self.full_name, other.full_name))

class HouseKim(HousePark):
    __last_name__ = "김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가네." %(self.full_name, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet
