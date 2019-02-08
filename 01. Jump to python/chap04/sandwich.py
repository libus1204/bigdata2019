ingredient_list=[]
print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.")
print("1. 주문")
print("2. 종료")
input_num = int(input("입력 : "))
def input_ingredient():
    while True:
        ingredient_list.append(str(input("안녕하세요. 원하시는 재료를 입력하세요: ")))
        for i in ingredient_list:
           if i == "종료" : return ingredient_list

def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list:
        if i == "종료":
            print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")
            break
        else: print(i+"를 추가합니다.")
if input_num == 1:
    input_ingredient()
    make_sandwiches(ingredient_list)
else: print("종료합니다")