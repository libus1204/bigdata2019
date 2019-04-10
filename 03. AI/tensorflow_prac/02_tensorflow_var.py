import tensorflow as tf

# a = tf.constant(1) # 어떠한 텐서 자료를 반환.
# b = tf.constant(2)
# c = tf.add(a, b) # a, b 더함
#
# sess = tf.Session()
# print(sess.run(c))
# print(c)
sess = tf.Session()
a = tf.Variable(5)
b = tf.Variable(3)
c = tf.multiply(a, b)

init = tf.global_variables_initializer() # tensorflow 적용할수 있는 형태로 초기화
sess.run(init)
print(sess.run(c))

a = tf.Variable(15)
c = tf.multiply(a, b)
init = tf.global_variables_initializer() # tensorflow 적용할수 있는 형태로 초기화
sess.run(init)
print(sess.run(c))