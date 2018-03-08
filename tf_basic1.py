import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)

sess = tf.Session()
print(sess.run(result))
sess.close()

with tf.Session() as sess:  # will automatically close the session when done
    output = sess.run(result)
    print(output)