import tensorflow as tf

# tf graph input
X = [1, 2, 3]
Y = [1, 2, 3]

# Set wrong model weights
W = tf.Variable(5.0)

# Linear Model
hypothesis = X * W

# Manual Gradient
gradient = tf.reduce_mean((W * X - Y) * X) * 2

# cost function
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)

# Get gradients
gvs = optimizer.compute_gradients(cost)

# Apply gradients
apply_gradients = optimizer.apply_gradients(gvs)

# Launch the graph in a sesson
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run([gradient, W, gvs]))
    sess.run(apply_gradients)
