import tensorflow as tf

# MNIST 데이터를 다운로드
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

# 변수들 설정
X = tf.placeholder(tf.float32, [None, 784])  # mnist 이미지 데이터 형태는 28 * 28
Y = tf.placeholder(tf.float32, [None, 10])  # 0-9 숫자분류 => 10 classes

# Logistic Classifier (Linear Classifier)
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

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
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 배치 크기는 100
    sess.run(train_step, feed_dict = {X: batch_xs, Y: batch_ys})

# 학습된 모델이 얼마나 정확한지를 계산하고 출력
correct_prediction = tf.equal(tf.argmax(softmax_y, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict = {X: mnist.test.images, Y: mnist.test.labels}))


