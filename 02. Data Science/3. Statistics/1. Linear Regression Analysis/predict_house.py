import pandas as pd
import numpy as np
from statsmodels.formula.api import ols, glm
from itertools import combinations

house = pd.read_csv('Housing.csv', sep=',', header=0)

house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)
columns_list = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'garagepl', 'driveway01',
                'recroom01', 'fullbase01', 'gashw01', 'airco01', 'prefarea01']
count = 0
max = 0
max_list_final = []
max_list_final1 = []
max_list_final2 = []
max_list_final3 = []

error1 = 0.05
error2 = 0.1
error3 = 0.2
for number in range(1, 12):
    combination_list = list(combinations(columns_list, number))
    for tuple in combination_list:
        print(count)
        my_formula = 'price ~ '
        list_ = []
        list_1 = []
        list_2 = []
        list_3 = []
        for data in tuple:
            my_formula += '%s + ' % data
            list_.append(data)
            list_1.append(data)
            list_2.append(data)
            list_3.append(data)
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        dependent_variable = house['price']
        independent_variables = house[list(tuple)]
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        match_count1 = 0
        match_count2 = 0
        match_count3 = 0
        max_list = []
        max_list1 = []
        max_list2 = []
        max_list3 = []
        count += 1
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
            if y_predicted_rounded[index] >= (int(dependent_variable.values[index]) - \
                int(dependent_variable.values[index])*error1) and \
                    y_predicted_rounded[index] <= (int(dependent_variable.values[index]) + \
                                               int(dependent_variable.values[index]) * error1):
                match_count1 += 1
            if y_predicted_rounded[index] >= (int(dependent_variable.values[index]) - \
                int(dependent_variable.values[index])*error2) and \
                    y_predicted_rounded[index] <= (int(dependent_variable.values[index]) + \
                                               int(dependent_variable.values[index]) * error2):
                match_count2 += 1
            if y_predicted_rounded[index] >= (int(dependent_variable.values[index]) - \
                int(dependent_variable.values[index])*error3) and \
                    y_predicted_rounded[index] <= (int(dependent_variable.values[index]) + \
                                               int(dependent_variable.values[index]) * error3):
                match_count3 += 1
        print('\n >> ' + my_formula.replace('price ~ ', ''))
        print(" >> 정답률 : %.2f %%" % (match_count / len(y_predicted_rounded) * 100))
        print(" >> 정답률(0.05) : %.2f %%" % (match_count1 / len(y_predicted_rounded) * 100))
        print(" >> 정답률(0.1)  : %.2f %%" % (match_count2 / len(y_predicted_rounded) * 100))
        print(" >> 정답률(0.2)  : %.2f %%" % (match_count3 / len(y_predicted_rounded) * 100))
        max_list.append(match_count/len(y_predicted_rounded)*100)
        max_list.append(list_)
        max_list_final.append(max_list)
        max_list1.append(match_count1 / len(y_predicted_rounded) * 100)
        max_list1.append(list_1)
        max_list_final1.append(max_list1)
        max_list2.append(match_count2 / len(y_predicted_rounded) * 100)
        max_list2.append(list_2)
        max_list_final2.append(max_list2)
        max_list3.append(match_count3 / len(y_predicted_rounded) * 100)
        max_list3.append(list_3)
        max_list_final3.append(max_list3)

max_list_final = sorted(max_list_final, reverse=True)
print(max_list_final[0])

max_list_final1 = sorted(max_list_final1, reverse=True)
print(max_list_final1[0])

max_list_final2 = sorted(max_list_final2, reverse=True)
print(max_list_final2[0])

max_list_final3 = sorted(max_list_final3, reverse=True)
print(max_list_final3[0])
# my_formula = 'price ~ lotsize + bedrooms + bathrms + stories + garagepl + driveway01 + recroom01 +' \
#              'fullbase01 + gashw01 + airco01 + prefarea01'
lm = ols(my_formula, data=house).fit()
# print(" < lm.summary() > ")
# print(lm.summary())
#