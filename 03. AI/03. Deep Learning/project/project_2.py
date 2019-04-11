import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

bp = pd.read_csv('blood_pressure.csv')

bp_mapping = {'low':0, 'normal':1, 'high':2}

bp['blood_pressure'] = bp['blood_pressure'].map(bp_mapping)

data_train, data_test, label_train, label_test = train_test_split(bp[['systole', 'atonly']], bp['blood_pressure'])

X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2, 1], name = 'weight'))
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

cost = tf.reduce_mean(tf.square(hypothesis - Y))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

previous_cost = 0
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10000):
        cost_val, _ = sess.run([cost, train], feed_dict={X:data_train, Y:data_test})
        if step % 500 == 0:
            print("Ste = ", step, ", Cost : ", cost_val)
        if previous_cost == cost_val:
            print("found best hypothesis when step : ", step, "\n")
            break
        else:
            previous_cost = cost_val
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict = {X: data_train, Y: data_test})
    print("\n Accuracy : ", a)
    print("\n Test CSV runningResult")
    h2, c2, a2 = sess.run([hypothesis, predicted, accuracy], feed_dict={X:label_train, Y:label_test})
    print("\n Accuracy : ", a2)
    print("end")

