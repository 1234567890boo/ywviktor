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
#Must be initialized in the session beofre being used Example: c.initialize.run()
# or can be writen like this:
'''init=tf.global_variables_intializer()
with tf.Session() as sess:
    sess.run(init)'''


#tensor an array of numbers or functions that can be changed(aka node in machiene learning)

sess = tf.Session() #The lines conecting the tensors, works like a function. S is capital
#some statements
sess.close()

'''
basic math can be done in the varibales
Ex: c=(2*a)+(3*b)

Straight line regression: y=mx+b
can predict m and b from x and wrong m and b

Squared delta is the difference of predicted and correct answer
Ex: Squared_Delta=tf.square(model-y)

Loss is the total of the squared delta, and shows how wrong the computer was.
0 is 100% correct and the higher the number, the more wrong it is
Ex: loss=tf.reduce_sum(Squared_Delta)

Optimzer is the AI part of the code. Adaam Optimizer is the one i am goingt o use, but there are more than that
Some of them can't work and there will be new, better ones in the future
An iteration is called an epoch, and thousands of epochs can be made in a neuran network
Ex: Opitmizer=tf.train.AdamOptimizer(0.1)
    train=opimizer.minimize(loss)
'''