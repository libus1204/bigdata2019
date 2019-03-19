import pandas as pd
from sklearn import svm, metrics

or_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
xor_df = pd.DataFrame(or_input)
xor_data = xor_df.iloc[:, 0:2] # 데이터
xor_label = xor_df.iloc[:, 2] # 레이블

# 데이터 학습과 예측하기
clf = svm.SVC(gamma='auto')
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", ac_score*100)