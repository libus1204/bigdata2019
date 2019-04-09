import tensorflow as tf

ta = tf.zeros((2, 2))

session = tf.InteractiveSession()
print(ta.eval())
session.close()