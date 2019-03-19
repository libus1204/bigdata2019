import pandas as pd
from statsmodels.formula.api import ols, glm
import operator
from itertools import combinations

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

match_dic = {}
count = 0
columns_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH',
               'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']

for number in range(1, 12):
    combination_list = list(combinations(columns_list, number))
    for tuple in combination_list:
        print(count)
        my_formula = 'quality ~ '
        for data in tuple:
            my_formula += '%s + ' % data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        indendent_variables = wine[list(tuple)]
        y_predicted = lm.predict(indendent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        count += 1
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
        print("\n>> 조합 : %s" % my_formula.replace('quality ~ ', ''))
        print(" 정답률 : %.2f %%" % (match_count/len(y_predicted_rounded)*100))
        match_dic['%s' % my_formula.replace('quality ~ ', '')] = match_count/len(y_predicted_rounded)*100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print("최대값 조합 : %s, %.2f %%" % (match_dic[0][0], match_dic[0][1]))

lm = ols('quality ~ ' + match_dic[0][0], data=wine).fit()
print(" < lm.summary() > ")
print(lm.summary())