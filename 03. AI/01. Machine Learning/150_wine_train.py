import pandas as pd
from sklearn import svm, metrics
from itertools import combinations
import operator
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
wine_df = pd.DataFrame(wine)

wine_data = wine_df.iloc[:, 1:12]
wine_label = wine_df.iloc[:, 12]
clf = svm.SVC(gamma='auto')
clf.fit(wine_data, wine_label)
pre = clf.predict(wine_data)
ac_score = metrics.accuracy_score(wine_label, pre)
print("정답률 : ", ac_score*100)
match_dic = {}
columns_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH',
               'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
count = 0
for number in range(1, len(columns_list)+1):
    combination_list = list(combinations(columns_list, number))
    for tup in combination_list:
        print(count)
        wine_data = wine[list(tup)]
        clf = svm.SVC(gamma='auto')
        clf.fit(wine_data, wine_label)
        pre = clf.predict(wine_data)
        ac_score = metrics.accuracy_score(wine_label, pre)
        combination_str = '+'.join(list(tup))
        print('\n>> 조합: %s' % (combination_str.rstrip('+')))
        ok = 0; total = 0
        for idx, answer in enumerate(wine_label):
            p = pre[idx]
            if p == answer : ok += 1
            total += 1
        print("정답률 : ", ok, "/", total, "=", ok/total*100)
        # print('>> 정답률: %.2f %%' % (ac_score*100))
        match_dic['%s' % (combination_str.rstrip('+'))] = ok/total*100
        count += 1
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print('총 조합 갯수: %d' % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))