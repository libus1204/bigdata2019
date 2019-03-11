import csv
import math


def get_csv_row_instance(primary_key): # 행 리턴
    for row_count in range(len(data)):
        if primary_key in data[row_count]:
            return data[row_count]

def get_csv_col_instance(col_name): # 열 리턴
    col_instance=[]
    for col_count in range(len(data[0])):
        if col_name == data[0][col_count]:
            for count in range(len(data)):
                col_instance.append(data[count][col_count])
    return col_instance

def My_Sum(data_list):
    My_Sum=0
    for count in range(1, len(data_list)):
        My_Sum += int(data_list[count])
    return My_Sum

def My_Average(data_list):
    My_Average = My_Sum(data_list)/(len(data)-1)
    return My_Average

def My_Max(data_list):
    My_Max=0
    for count in range(1, len(data_list)):
        if My_Max < int(data_list[count]):
            My_Max = int(data_list[count])
        else: pass
    return My_Max

def My_Min(data_list):
    My_Min = 0
    for count in range(1, len(data_list)):
        if My_Min > int(data_list[count]):
            My_Min = int(data_list[count])
        else: pass
    return My_Min

def My_Deviation(data_list):  # 표본값 - 평균
    get_csv_col_instance(get_access)
    print("표본\t편차")
    for count in range(1, len(data_list)):
        print("%s\t%s" % (get_csv_col_instance(get_access)[count],
                          int(get_csv_col_instance(get_access)[count])-My_Average(data_list)))

def My_Standard_Deviation(data_list): # 표준편차(Standard Deviation) 공식: √분산
    Variance = math.sqrt(My_Variance(data_list))
    return Variance

def My_Variance(data_list): # 분산(Variance) 공식: ∑(표본-평균)**2/표본수
    My_Variance=0
    for count in range(1, len(data_list)):
        my_dev = int(get_csv_col_instance(get_access)[count])-My_Average(data_list)
        My_Variance += my_dev ** 2
    My_Variance = My_Variance/(len(data_list)-1)
    return My_Variance

def My_Ascendant(data_list): # 오름차순
    data_list.pop(0)
    data_list = map(int, data_list)
    data_list = sorted(data_list)
    for count in data_list:
        print(count, end=" ")

def My_Descendant(data_list): # 내림차순
    data_list.pop(0)
    data_list = map(int, data_list)
    data_list = sorted(data_list)
    data_list = reversed(data_list)
    for count in data_list:
        print(count, end=" ")
    pass

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))

while True:
    print("\n<CSV Handle 연습예제>")
    print("0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬")
    menu_num = input("메뉴를 입력하세요 : ")
    if menu_num == '0':
        print("프로그램을 종료합니다")
        break
    elif menu_num == '1':
        primary_key = input("JURISDICTION NAME 을 입력하세요 : ")
        for count in range(len(get_csv_row_instance(primary_key))):
            print(get_csv_row_instance(primary_key)[count], end=" ")
        print("")
    elif menu_num == '2':
        col_name = input("Access Key 를 입력하세요 : ")
        for count in range(1, len(data)):
            print(get_csv_col_instance(col_name)[count])
    elif menu_num == '3':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        for count in range(1, len(data)):
            print(get_csv_col_instance(get_access)[count])
        print("총합 : %s" % My_Sum(data_list))
    elif menu_num == '4':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        for count in range(1, len(data)):
            print(get_csv_col_instance(get_access)[count])
        print("평균 : %s" % My_Average(data_list))
    elif menu_num == '5':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        for count in range(1, len(data)):
            print(get_csv_col_instance(get_access)[count])
        print("최대값 : %s" % My_Max(data_list))
    elif menu_num == '6':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        for count in range(1, len(data)):
            print(get_csv_col_instance(get_access)[count])
        print("최소값 : %s" % My_Min(data_list))
    elif menu_num == '7':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        print("편차(Deviation) 공식 : 표본값 - 평균")
        My_Deviation(data_list)
    elif menu_num == '9':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        print("분산(Variance) 공식: ∑(표본-평균)**2/표본수")
        for count in range(1, len(data)):
            print(get_csv_col_instance(get_access)[count])
        print("분산 : %s" % My_Variance(data_list))
    elif menu_num == '8':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        print("표준편차(Standard Deviation) 공식: √분산")
        for count in range(1, len(data)):
            print(get_csv_col_instance(get_access)[count])
        print("표준편차 : %s" % My_Standard_Deviation(data_list))
    elif menu_num == '10':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        My_Ascendant(data_list)
    elif menu_num == '11':
        get_access = input("Access Key 를 입력하세요 : ")
        data_list = get_csv_col_instance(get_access)
        My_Descendant(data_list)