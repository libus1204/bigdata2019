import pandas as pd
import operator
from itertools import combinations
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

match = {}
columns_list = ['alcohol','chlorides','citric_acid','density','fixed_acidity','free_sulfur_dioxide','pH',
               'residual_sugar','sulphates','total_sulfur_dioxide','volatile_acidity']

for number in range(1, 12):
    combination_list = list(combinations(columns_list, number))
    for tuple in combination_list:
        my_formula = 'quality ~ '
        for data in tuple:
            my_formula += '%s +' % data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variables = wine[list(tuple)]
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
        print("\n>> " + my_formula.replace('quliaty ~ ', ''))
        print("match count = ", match_count)
        print("정답률 : %.2f %%" % (match_count/len(y_predicted_rounded)*100))
        match['%s' % my_formula.replace('quality ~ ', '')] = match_count/len(y_predicted_rounded)*100

match = sorted(match.items(), key=operator.itemgetter(1), reverse=True)
print("총 조합 갯수 : %d" % len(match))
print("최대값 조합 : %s, %.2f%%" % (match[0][0], match[0][1]))

lm = ols('quality ~ ' + match[0][0], data=wine).fit()
print(" < lm.summary() > ")
print(lm.summary())

