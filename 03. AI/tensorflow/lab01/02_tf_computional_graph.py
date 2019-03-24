import tensorflow as tf

# Build graph (tensors) using Tensorflow operations
node1 = tf.constant(3.0, tf.float32) # 데이터 타입
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1 : ", node1, "node2 : ", node2)
print("node3 : ", node3)

# feed data and run graph(operation)
sess = tf.Session()

# update variables in the graph
print("sess.run(node1, node2) : ", sess.run([node1, node2]))
print("sess.run(node3) : ", sess.run(node3))