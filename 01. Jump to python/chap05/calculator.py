class Calculator:
    def __init__(self, number_list):
        self.number_list = number_list
    def sum(self):
        total = 0
        for number in self.number_list:
            total += number
        return total
    def avg(self):
        total_sum = self.sum()
        average = total_sum / len(self.number_list)
        return average

if __name__ == "__main__":
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())
    cal2 = Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())