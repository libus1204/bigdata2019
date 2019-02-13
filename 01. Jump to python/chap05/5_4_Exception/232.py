class SMDenominiatorZeroError(Exception):
    pass
class Mydiv:
    num1 = 0
    num2 = 0
    def __init__(self, num1, num2):
        if num2 == 0:
            raise SMDenominiatorZeroError("Domination is Zero")
        self.num1 = num1
        self.num2 = num2
    def safe_div(self):
        result = self.num1 / self.num2
        print("%d / %d = %d 입니다." %(self.num1, self.num2, result))

try:
    my_cal = Mydiv(int(input("분자를 입력하세요 : ")), int(input("분모를 입력하세요 : ")))
    my_cal.safe_div()
except Exception as e:
    print(e)
