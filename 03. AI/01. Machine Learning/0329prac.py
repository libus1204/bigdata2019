import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np

house = pd.read_csv('Housing.csv', sep=',', header=0)
house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)

house_data = house[['lotsize', 'bedrooms', 'bathrms', 'stories', 'garagepl', 'driveway01',
                'recroom01', 'fullbase01', 'gashw01', 'airco01', 'prefarea01']]
house_label = house['price']
train_data, test_data, train_label, test_label = train_test_split(house_data, house_label)
clf = svm.SVC(gamma='auto')
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기
print(pre[0])

ac_score = metrics.accuracy_score(test_label, pre)
print("전체 데이터 수 : %d" % (len(house_data)))
print("학습 전용 데이터 수 : %d" % (len(train_data)))
print("테스트 데이터 수 : %d" % (len(test_data)))
print("정답률 : ", ac_score*100)
