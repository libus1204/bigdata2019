import pandas as pd
import math
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data_frame = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv', index_col=None)

def get_csv_row_instance(primary_key): # 행 리턴
    data_frame_row_condition = data_frame[data_frame['JURISDICTION NAME'].astype(str) == primary_key]
    return data_frame_row_condition

def get_csv_col_instance(col_name): # 열 리턴
    data_frame_col_condition = data_frame.loc[:, [col_name]]
    return data_frame_col_condition

def My_Sum(get_access):
    total_sum = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, get_access]).sum()
    return total_sum

def My_Average(get_access):
    average = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, get_access]).mean()
    return average

def My_Max(get_access):
    max = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, get_access]).max()
    return max

def My_Min(get_access):
    min = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, get_access]).min()
    return min

def My_Deviation(get_access):  # 표본값 - 평균
    for count in range(len(get_csv_col_instance(get_access))):
        print("%0.1f\t%s" % (float(get_csv_col_instance(get_access).values[count]),
                              float(get_csv_col_instance(get_access).values[count]) -
                              (float(My_Average(get_access)))))

def My_Variance(get_access): # 분산(Variance) 공식: ∑(표본-평균)**2/표본수
    # variance = 0
    # for count in range(len(get_csv_col_instance(get_access))):
    #     a = float(get_csv_col_instance(get_access).values[count]) - (float(My_Average(get_access)))
    #     variance += a ** 2
    # variance = variance/(len(get_csv_col_instance(get_access)))
    # return variance # 값 1865.1986498132708
    variance = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, get_access]).var()
    return variance # 값 1873.135665

def My_Standard_Deviation(get_access): # 표준편차(Standard Deviation) 공식: √분산
    # stand_dev = pd.DataFrame(int(str(value)) for value in data_frame.loc[:, get_access]).mad()
    stand_dev = math.sqrt(My_Variance(get_access))
    return stand_dev

def My_Ascendant(get_access): # 오름차순
    ascendant = pd.DataFrame(data_frame.loc[:, get_access])
    print(ascendant.sort_values(by=get_access))

def My_Descendant(get_access): # 내림차순
    ascendant = pd.DataFrame(data_frame.loc[:, get_access])
    print(ascendant.sort_values(by=get_access, ascending=False))


while True:
    print("\n<CSV Handle 연습예제>")
    print("0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬")
    menu_num = input("메뉴를 입력하세요 : ")
    if menu_num == '0':
        print("프로그램을 종료합니다")
        break
    elif menu_num == '1':
        primary_key = input("JURISDICTION NAME 을 입력하세요 : ")
        print(get_csv_row_instance(primary_key))
    elif menu_num == '2':
        col_name = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(col_name))
    elif menu_num == '3':
        get_access = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(get_access))
        print("총합 : %s" % My_Sum(get_access))
    elif menu_num == '4':
        get_access = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(get_access))
        print("평균 : %s" % My_Average(get_access))
    elif menu_num == '5':
        get_access = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(get_access))
        print("최대값 : %s" % My_Max(get_access))
    elif menu_num == '6':
        get_access = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(get_access))
        print("최소값 : %s" % My_Min(get_access))
    elif menu_num == '7':
        get_access = input("Access Key 를 입력하세요 : ")
        print("편차(Deviation) 공식 : 표본값 - 평균")
        print("표본\t\t\t\t편차")
        My_Deviation(get_access)
    elif menu_num == '9':
        get_access = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(get_access))
        print(My_Variance(get_access))
    elif menu_num == '8':
        get_access = input("Access Key 를 입력하세요 : ")
        print(get_csv_col_instance(get_access))
        print("표준편차(Standard Deviation) 공식: √분산")
        print("표준편차 : " +My_Standard_Deviation(get_access))
    elif menu_num == '10':
        get_access = input("Access Key 를 입력하세요 : ")
        My_Ascendant(get_access)
    elif menu_num == '11':
        get_access = input("Access Key 를 입력하세요 : ")
        My_Descendant(get_access)