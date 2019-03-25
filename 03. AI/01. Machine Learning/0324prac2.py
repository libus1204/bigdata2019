# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# import pandas as pd
#
# test_bmi_label = pd.read_csv("bmi.csv")
#
# label_for_test = test_bmi_label["label"]
# weight = test_bmi_label["weight"] / 100
# height = test_bmi_label["height"] / 200
# wh = pd.concat([weight, height], axis = 1)
#
# data_train, data_test, label_train, label_test = train_test_split(wh, label_for_test)
#
# clf = svm.SVC(gamma="auto")
# clf.fit(data_train, label_train)
#
# predict = clf.predict(data_test)
#
# ac_score = metrics.accuracy_score(label_test, predict)
# cl_report = metrics.classification_report(label_test, predict)
# print("정답률 : ", ac_score)
# print("리포트 = \n", cl_report)
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# import pandas as pd
# test_bmi = pd.read_csv("bmi.csv")
# label = test_bmi["label"]
# weight = test_bmi["weight"] / 100
# height = test_bmi["height"] / 200
# wh = pd.concat([weight, height], axis = 1)
# data_train, data_test, label_train, label_test = train_test_split(wh, label)
# clf = svm.SVC(gamma="auto")
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac_score = metrics.accuracy_score(label_test, predict)
# cl_report = metrics.classification_report(label_test, predict)
# print("정답률 : ", ac_score)
# print("리포트 : \n", cl_report)
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# import pandas as pd
# test_bmi = pd.read_csv("bmi.csv")
# label = test_bmi["label"]
# weight = test_bmi["weight"] / 100
# height = test_bmi["height"] / 200
# w_and_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_and_h, label)
# clf = svm.SVC(gamma="auto")
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac_score = metrics.accuracy_score(label_test, predict)
# cl_report = metrics.classification_report(label_test, predict)
# print(ac_score)
# print(cl_report)
# import pandas as pd
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# test = pd.read_csv("bmi.csv")
# label = test["label"]
# weight = test["weight"] / 100
# height = test["height"] / 200
# w_and_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_and_h, label)
# clf = svm.SVC(gamma="auto")
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac_score = metrics.accuracy_score(label_test, predict)
# cl_report = metrics.classification_report(label_test, predict)
# print(ac_score)
# print(cl_report)
# import pandas as pd
# from sklearn import svm, metrics
# from sklearn.model_selection import  train_test_split
# test = pd.read_csv("bmi.csv")
# label = test["label"]
# weight = test["weight"] / 100
# height = test["height"] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma="auto")
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)
# import pandas as pd
# from sklearn import metrics, svm
# from sklearn.model_selection import train_test_split
# test = pd.read_csv('bmi.csv')
# label = test['label']
# weight = test['weight'] / 100
# height = test['height'] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma="auto")
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)
# import pandas as pd
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# test = pd.read_csv('bmi.csv')
# label = test['label']
# weight = test['weight'] / 100
# height = test['height'] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn import svm, metrics
# test = pd.read_csv('bmi.csv')
# label = test['label']
# weight = test['weight'] / 100
# height = test['height'] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn import svm, metrics
# test = pd.read_csv('bmi.csv')
# label = test['label']
# weight = test['weight'] / 100
# height = test['height'] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn import svm, metrics
# test = pd.read_csv('bmi.csv')
# label = test['label']
# weight = test['weight'] / 100
# height = test['height'] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)
# import pandas as pd
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# bmi_for_test = pd.read_csv('bmi.csv')
# label = bmi_for_test['label']
# weight = bmi_for_test['weight'] / 85
# height = bmi_for_test['height'] / 200
# w_h = pd.concat([weight, height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(w_h, label)
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)
# import pandas as pd
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# test_bmi_label = pd.read_csv('bmi.csv')
# test_label = test_bmi_label['label']
# test_weight = test_bmi_label['weight'] / 85
# test_height = test_bmi_label['height'] / 200
# test_w_and_h = pd.concat([test_weight, test_height], axis=1)
# data_train, data_test, label_train, label_test = train_test_split(test_w_and_h, test_label)
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)
# predict = clf.predict(data_test)
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print(ac)
# print(cl)















# import pandas as pd
# from sklearn import metrics, svm
# from sklearn.model_selection import train_test_split

# 데이터 읽기
# test_bmi_label = pd.read_csv('bmi.csv')

# 데이터 레이블 분리
# test_label = test_bmi_label['label']
# test_weight = test_bmi_label['weight'] / 85
# test_height = test_bmi_label['height'] / 200
# test_weight_and_height = pd.concat([test_weight, test_height], axis=1)

# 학습 데이터와 테스트 전용 데이터로 나누기
# data_test, data_train, label_test, label_train = train_test_split(test_weight_and_height, test_label)

# 학습
# clf = svm.SVC(gamma='auto')
# clf.fit(data_train, label_train)

# 예측
# predict = clf.predict(data_test)

# 결과 테스트
# ac = metrics.accuracy_score(label_test, predict)
# cl = metrics.classification_report(label_test, predict)
# print("정답률 : ", ac * 100)
# print("리포트 : ", cl)
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 데이터 읽기
bmi = pd.read_csv('bmi.csv')

# 데이터 레이블 나누기
l = bmi['label']
w = bmi['weight'] / 85  # 표준화
h = bmi['height'] / 200 # 표준화
w_h = pd.concat([w, h], axis=1)

# 학습 데이터와 테스트 전용 데이터 나누기
data_train, data_test, label_train, label_test = train_test_split(w_h, l)

# 학습
clf = svm.SVC(gamma='auto')
clf.fit(data_train, label_train)

# 예측
predict = clf.predict(data_test)
ac = metrics.accuracy_score(label_test, predict)
cl = metrics.classification_report(label_test, predict)

print(ac)
print(cl)

