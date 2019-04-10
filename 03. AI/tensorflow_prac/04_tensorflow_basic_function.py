import tensorflow as tf

a = tf.constant(17)
b = tf.constant(5)
sess = tf.Session()
# 덧셈
c = tf.add(a, b)
print(sess.run(c))

# 뺄셈
c = tf.subtract(a, b)
print(sess.run(c))

# 곱셈
c = tf.multiply(a, b)
print(sess.run(c))

# 나눗셈
c = tf.truediv(a, b)
print(sess.run(c))

# 나머지
c = tf.mod(a, b)
print(sess.run(c))

# 절댓값
c = tf.abs(-a)
print(sess.run(c))

a = tf.constant(17.5)
b = tf.constant(5.0)

# 음수ㅡ
c = tf.negative(a)
print(sess.run(c))

# 부호 반환
c = tf.sign(a)
print(sess.run(c))

# 제곱
c = tf.square(a)
print(sess.run(c))

# 거듭제곱

c = tf.pow(a, 4)
print(sess.run(c))

# 더 큰값확인
c = tf.maximum(a, b)
print(sess.run(c))

c = tf.minimum(a, b)
print(sess.run(c))

c = tf.exp(b)
print(sess.run(c))

c = tf.log(b)
print(sess.run(c))

c = tf.sin(a)
print(sess.run(c))