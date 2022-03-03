import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a=tf.constant(3)
b=tf.constant(4)
c=a*b
sess=tf.Session()
out1=sess.run(c)
print(out1)
sess.close()