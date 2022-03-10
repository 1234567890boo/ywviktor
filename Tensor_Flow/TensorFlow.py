import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a=tf.Variable(2)
b=tf.Variable(3)
c=(2*a)+(3*b)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    out1=sess.run(c)
    print(out1)