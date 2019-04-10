import tensorflow as tf

# input = [1, 2, 3, 4, 5]
# x = tf.placeholder(dtype=tf.float32)
# y = x + 5
#
# sess = tf.Session()
#
# print(sess.run(y, feed_dict={x: input}))

mathScore = [85, 99, 84, 97, 92]
englishScore = [59, 80, 84, 68, 77]

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
y = (a + b) / 2

sess = tf.Session()
print(sess.run(y, feed_dict={a: mathScore, b: englishScore}))
