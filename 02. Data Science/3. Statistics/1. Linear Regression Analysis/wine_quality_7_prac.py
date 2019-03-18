import pandas as pd
from statsmodels.formula.api import ols,glm
import operator
from itertools import combinations
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
print("7.2.7 예측하기")
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ', '_')

match_dic={}
columns_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH',
               'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
count = 0
for num in range(1, 12):
    combination_list = list(combinations(columns_list, num))
    for tup in combination_list:
        print(count)
        my_formula = 'quality ~ '
        for data in tup:
            my_formula += '%s + ' % data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variables = wine[list(tup)]
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        count += 1
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
        print('\n>> ' + my_formula.replace('quality ~ ', ''))
        print('>> match count = ', match_count)
        print('>> 정답률 : %.2f %%' % (match_count/len(y_predicted_rounded)*100))
        match_dic['%s' % my_formula.replace('quality ~ ', '')] = match_count/len(y_predicted_rounded)*100
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print('총 조합 갯수: %d' % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
end = datetime.fromtimestamp(time.time())
print(start)
print(end)
print(end-start)