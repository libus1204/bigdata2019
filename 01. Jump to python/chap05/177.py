class Service:
    secret = "영구는 배꼽이 두 개다."
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a+b
        print("%s님 %s + %s = %s 입니다." % (self.name, a, b, result))

pey = Service()
pey.setname("홍길동")
# print(pey.secret)
# pey.sum(pey,1,1)
pey.sum(1,1) #  pey.sum 을 통하여 pey가 호출한 지 알기 때문에 pey는 생략 가능
# pey.sum("1", "1")
