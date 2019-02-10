class HouseKim:
    lastname = "김"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다." %(self.fullname, where))

pey = HouseKim("상민")
pey.travel("Canada")

