# Data Source: www.kaggle.com/c/titanic
import tensorflow as tf

# MNIST 데이터를 다운로드 한다.
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 수집 데이터 형식 기술
# 데이터 요약: 손글씨 그림 이미지
# 고정 변수: 그림의 픽셀 정보
# 종속 변수: 0~9까지 숫자 판별
# 상세 필드 사항 아래 참조
# TRAINING SET LABEL FILE (train-labels-idx1-ubyte):
# [offset] [type]          [value]          [description]
# 0000     32 bit integer  0x00000801(2049) magic number (MSB first)
# 0004     32 bit integer  60000            number of items
# 0008     unsigned byte   ??               label
# 0009     unsigned byte   ??               label
# ........
# xxxx     unsigned byte   ??               label
# The labels values are 0 to 9.
#
# TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
# [offset] [type]          [value]          [description]
# 0000     32 bit integer  0x00000803(2051) magic number
# 0004     32 bit integer  60000            number of images
# 0008     32 bit integer  28               number of rows
# 0012     32 bit integer  28               number of columns
# 0016     unsigned byte   ??               pixel
# 0017     unsigned byte   ??               pixel
# ........
# xxxx     unsigned byte   ??               pixel
# Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
#
# TEST SET LABEL FILE (t10k-labels-idx1-ubyte):
# [offset] [type]          [value]          [description]
# 0000     32 bit integer  0x00000801(2049) magic number (MSB first)
# 0004     32 bit integer  10000            number of items
# 0008     unsigned byte   ??               label
# 0009     unsigned byte   ??               label
# ........
# xxxx     unsigned byte   ??               label
# The labels values are 0 to 9.
#
# TEST SET IMAGE FILE (t10k-images-idx3-ubyte):
# [offset] [type]          [value]          [description]
# 0000     32 bit integer  0x00000803(2051) magic number
# 0004     32 bit integer  10000            number of images
# 0008     32 bit integer  28               number of rows
# 0012     32 bit integer  28               number of columns
# 0016     unsigned byte   ??               pixel
# 0017     unsigned byte   ??               pixel
# ........
# xxxx     unsigned byte   ??               pixel

# 변수들을 설정한다.
X = tf.placeholder(tf.float32, [None, 784]) # mnist 이미지데이터 형태는 28 * 28 = 784
Y = tf.placeholder(tf.float32, [None, 10])  # 0-9 숫자분류 = > 10 classes

#Logistic Classifier (Linear Classifier)
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
#matmul: 행렬 내적(곱)
logit_y = tf.matmul(X, W) + b

# softmax와 cross-entropy 모델을 설정한다.
softmax_y = tf.nn.softmax(logit_y)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# 경사하강법으로 모델을 학습한다.
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100) #배치크기는 100
  sess.run(train_step, feed_dict={X: batch_xs, Y: batch_ys})

# 결과 예측
correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))

# 결과 검증
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))

'''
#실행결과
Extracting MNIST_data/train-images-idx3-ubyte.gz
Extracting MNIST_data/train-labels-idx1-ubyte.gz
Extracting MNIST_data/t10k-images-idx3-ubyte.gz
Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
정확도 :  0.9092
'''