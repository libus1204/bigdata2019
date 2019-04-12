import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

bp = pd.read_csv('blood_pressure.csv')

# 수집 데이터 포맷 명시
# - 데이터 요약 : 심장 혈압 수치와 그에 따른 상태
# - 고정 변수 명시: 심장의 수축기, 이완기 시의 최대/최소 혈압
# - 종속 변수 명시: 사람의 상태
# - 각각의 필드의 의미 명시
# RangeIndex: 7031 entries, 0 to 7030
# Data columns (total 3 columns):
# systole           7031 non-null int64
# atony            7031 non-null int64
# blood_pressure    7031 non-null object
# dtypes: int64(2), object(1)

# 값 보정
bp['systole'] = bp['systole']/160
bp['atony'] = bp['atony']/130

# label 형태가 low, high, normal 중 1개의 값씩 들어가 있으므로
# low : [1. 0. 0.]
# normal : [0. 1. 0.]
# high : [0. 0. 1.]
# 인덱싱하여 전처리
bp_mapping = {'low':[1., 0., 0.], 'normal':[0., 1., 0.], 'high':[0., 0., 1.]}
bp['blood_pressure'] = bp['blood_pressure'].map(bp_mapping)

# 학습 / 테스트 전용 데이터 분리
data_train, data_test, label_train, label_test = train_test_split(bp[['systole', 'atony']], bp['blood_pressure'])

# 변수들 설정
X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 3])

# Logistic Classifier (Linear Classifier)
W = tf.Variable(tf.zeros([2, 3]))
b = tf.Variable(tf.zeros([3]))

# matmul : 행렬 내적(곱)
logit_y = tf.matmul(X, W) + b

# softmax 와 cross-entropy 모델 설정
softmax_y = tf.nn.softmax(logit_y)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y), reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# 경사하강법으로 모델 학습
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
data_train = data_train.values.tolist()
data_test = data_test.values.tolist()
label_train = label_train.values.tolist()
label_test = label_test.values.tolist()
for i in range(5000):
    sess.run(train_step, feed_dict = {X: data_train, Y: label_train})
correct_prediction = tf.equal(tf.argmax(softmax_y, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict = {X: data_test, Y: label_test}))




