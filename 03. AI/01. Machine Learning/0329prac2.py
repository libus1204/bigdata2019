import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
wine_data = wine[['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', \
            'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']]
wine_label = wine['quality']
train_data, test_data, train_label, test_label = train_test_split(wine_data, wine_label)
clf = svm.SVC(gamma='auto')
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기
print(pre)
ac_score = metrics.accuracy_score(test_label, pre)
print("전체 데이터 수 : %d" % (len(wine_data)))
print("학습 전용 데이터 수 : %d" % (len(train_data)))
print("테스트 데이터 수 : %d" % (len(test_data)))
print("정답률 : ", ac_score*100)