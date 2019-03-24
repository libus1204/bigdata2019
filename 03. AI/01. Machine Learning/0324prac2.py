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
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import  train_test_split
test = pd.read_csv("bmi.csv")
label = test["label"]
weight = test["weight"] / 100
height = test["height"] / 200
w_h = pd.concat([weight, height], axis=1)
data_train, data_test, label_train, label_test = train_test_split(w_h, label)
clf = svm.SVC(gamma="auto")
clf.fit(data_train, label_train)
predict = clf.predict(data_test)
ac = metrics.accuracy_score(label_test, predict)
cl = metrics.classification_report(label_test, predict)
print(ac)
print(cl)