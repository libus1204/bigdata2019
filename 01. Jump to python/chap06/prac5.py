class InputError1(Exception):
    pass
class InputError2(Exception):
    pass
class InputError3(Exception):
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
        try:
            if num2 == '0':
                raise InputError3("죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어선 안됩니다.")
        except Exception as e:
            print(e)
        self.num1 = int(num1)
        self.num2 = int(num2)
    def safe_sum(self):
        result = self.num1 + self.num2
        print("두 수의 덧셈은 : ", result)
    def safe_min(self):
        result = self.num1 - self.num2
        print("두 수의 뺄셈은 : ", result)
    def safe_mul(self):
        result = self.num1 * self.num2
        print("두 수의 곱셈은 : ", result)
    def safe_div(self):
        result = self.num1 / self.num2
        print("두 수의 나눗셈은 : ", result)
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
        my_cal.safe_min()
        my_cal.safe_mul()
        my_cal.safe_div()
    except Exception as e:
        pass