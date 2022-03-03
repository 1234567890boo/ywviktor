import tensorflow.compat.v1 as tf
tf.disable_v2_behaviour()

a = tf.constant(3)#Makes a constant with the value of 3, like a variable that cant be changed
'''tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const',
    verify_shape=False
) this is what can be put into a constant, can also be a list'''

b = tf.placeholder(tf.int32)#makes sure a piece of memory is not used temporarily
'''tf.placeholder(
    dtype,
    shape=None,
    name=None
) this i s what can be put into a placeholder, can also be a list'''

c = tf.Variable(5)#Makes a variable, must be initialized before being used, the V is capital.

#tensor an array of numbers or functions that can be changed(aka node in machiene learning)

sess = tf.Session() #The lines conecting the tensors, works like a function. S is capital
#some statements
sess.close()
