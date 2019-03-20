import pandas as pd
import numpy as np
from sklearn import svm, metrics
import operator
from itertools import combinations
house = pd.read_csv('Housing.csv', sep=',', header=0)
house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)
columns_list = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway01', 'recroom01', 'fullbase01',
                     'gashw01', 'airco01', 'prefarea01', 'garagepl']
house_data = house[columns_list]
house_label = house['price']
clf = svm.SVC(gamma='auto')
clf.fit(house_data, house_label)
pre = clf.predict(house_data)
ac_score = metrics.accuracy_score(house_label, pre)
print("정답률 : ", ac_score*100)
# zzzz
match_dic = {}


for number in range(1, len(columns_list)+1):
    combination_list = list(combinations(columns_list, number))
    for tup in combination_list:
        house_data = house[list(tup)]
        clf = svm.SVC(gamma='auto')
        clf.fit(house_data, house_label)
        pre = clf.predict(house_data)
        ac_score = metrics.accuracy_score(house_label, pre)
        combination_str = '+'.join(list(tup))
        print('\n>> 조합: %s' % (combination_str.rstrip('+')))
        ok = 0; total = 0
        for idx, answer in enumerate(house_label):
            p = pre[idx]
            if p == answer : ok += 1
            total += 1
        print("정답률 : ", ok, "/", total, "=", ok/total*100)
        # print('>> 정답률: %.2f %%' % (ac_score*100))
        match_dic['%s' % (combination_str.rstrip('+'))] = ok/total*100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print('총 조합 갯수: %d' % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))