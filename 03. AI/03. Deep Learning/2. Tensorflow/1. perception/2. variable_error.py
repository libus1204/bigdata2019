import tensorflow as tf

W1 = tf.zeros((3, 3))

W2 = tf.Variable(tf.zeros((2, 2)), name='weights')

session = tf.InteractiveSession()

print(W1.eval())
print(W2.eval()) # 초기화 되지 않았기 때문에 에러 발생

session.close()