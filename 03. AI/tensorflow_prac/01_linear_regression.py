import tensorflow as tf

xData = [1, 2, 3, 4, 5, 6, 7] # 하루 노동 시간
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000] # 하루 매출

W = tf.Variable(tf.random_uniform([1], -100, 100)) # weight
b = tf.Variable(tf.random_uniform([1], -100, 100)) # bias

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

H = W * X + b # 가설

cost = tf.reduce_mean(tf.square(H - Y))

a = tf.Variable(0.01) # 얼마나 점프하는가 스텝의 크기

optimizer = tf.train.GradientDescentOptimizer(a)  # 경사 하강 라이브러리

train = optimizer.minimize(cost)  # 가장 적게 만ㅁ드는 방향으로

init = tf.global_variables_initializer() # 변수 초기황

sess = tf.Session()

sess.run(init)

for i in range(10000):
    sess.run(train, feed_dict={X:xData, Y:yData})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict={X:xData, Y:yData}), sess.run(W), sess.run(b))
print(sess.run(H, feed_dict={X: [8]}))




