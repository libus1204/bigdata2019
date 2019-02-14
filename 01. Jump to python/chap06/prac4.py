class InputError1(Exception):
    pass
class InputError2(Exception):
    pass
class prac4_sum:
    def __init__(self, num1, num2):
        try:
            if num1.isdigit() == False:
                raise InputError1("죄송합니다. 첫 번째 입력이 [%s] 입니다. 숫자를 입력하세요." % num1)
        except Exception as e:
            print(e)
        try:
            if num2.isdigit() == False:
                raise InputError2("죄송합니다. 두 번째 입력이 [%s] 입니다. 숫자를 입력하세요." % num2)
        except Exception as e:
            print(e)
        self.num1 = int(num1)
        self.num2 = int(num2)
    def safe_sum(self):
        result = self.num1 + self.num2
        print(result)

while True:
    try:
        user_input = input("두 수를 입력하세요 : ").split()
        if user_input[0] =="종료" :
            print("프로그램을 종료합니다.")
            exit()
        num1 = user_input[0]
        num2 = user_input[1]
        my_cal = prac4_sum(num1, num2)
        my_cal.safe_sum()
    except Exception as e:
        pass



