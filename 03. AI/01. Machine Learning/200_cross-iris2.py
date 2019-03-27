# import pandas as pd
# from sklearn import svm, metrics, model_selection
# import random, re
# 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
# csv = pd.read_csv('iris.csv')
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기 --- (※2)
# data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
# label = csv["Name"]
# 크로스 밸리데이션하기 --- (※3)
# clf = svm.SVC()
# scores = model_selection.cross_val_score(clf, data, label, cv=5)
# print("각각의 정답률 =", scores)
# print("평균 정답률 =", scores.mean())

# import pandas as pd
# from sklearn import svm, metrics, model_selection
# iris_csv = pd.read_csv('iris.csv')
# data = iris_csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
# label = iris_csv['Name']
# clf = svm.SVC(gamma='auto')
# scores = model_selection.cross_val_score(clf, data, label, cv=5) # 회귀분석모형, 독립변수데이터, 종속변수데이터, 교차검증 생성기 객체
# print("각각의 정답률 : ", scores)
# print("평균 정답률 : ", scores.mean())
#
# import pandas as pd
# from sklearn import svm, model_selection
#
# # 붖꽃 데이터 불러오기
# iris_csv = pd.read_csv('iris.csv')
#
# # 종속 데이터 / 독립 데이터 구분
# data = iris_csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# label = iris_csv['Name']
#
# # 크로스 벨리데이션
# clf = svm.SVC(gamma='auto')
# scores = model_selection.cross_val_score(clf, data, label, cv=5)
# print(scores)
# print(scores.mean())

# import pandas as pd
# from sklearn import svm, model_selection
#
# # 붖꽃 데이터 불러오기
# csv = pd.read_csv('iris.csv')
#
# # 종속 / 독립 데이터 구분
# data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# label = csv['Name']
#
# # 크로스 밸리데이션
# clf = svm.SVC(gamma='auto')
# scores = model_selection.cross_val_score(clf, data, label, cv=5)
# print(scores)
# print(scores.mean())

# import pandas as pd
# from sklearn import svm, model_selection
#
# # 붖꽃 데이터 불러오기
# csv = pd.read_csv('iris.csv')
#
# # 독립/ 종속 데이터 구분
# data = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# label = csv['Name']
#
# # 크로스 밸리데이션
# clf = svm.SVC(gamma='auto')
# scores = model_selection.cross_val_score(clf, data, label, cv=5)
# print("각 정답률 : ", scores)
# print("평균 정답률 : ", scores.mean())

# import pandas as pd
# from sklearn import model_selection, svm
#
# # 붖꽃 데이터 불러오기
# iris_csv = pd.read_csv('iris.csv')
#
# # 독립 / 종속 데이터 구분
# data = iris_csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# label = iris_csv['Name']
#
# # 크로스 벨리데이션
# clf = svm.SVC(gamma='auto')
# scores = model_selection.cross_val_score(clf, data, label, cv=5)
# print("각각의 정답률 : ", scores)
# print("평균 정답률 : ", scores.mean())

import pandas as pd
from sklearn import model_selection, svm

# 붖꽃 데이터 불러오기
iris_file = pd.read_csv('iris.csv')

# 독립 / 종속 데이터 구분
data = iris_file[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
label = iris_file['Name']

# 머신 러닝 모델 생성
clf = svm.SVC(gamma='auto')

# 크로스 밸리데이션 하기
scores = model_selection.cross_val_score(clf, data, label, cv=5)

# 출력
print("각각의 정답률 : ", scores)
print("평균 정답률 : ", scores.mean())