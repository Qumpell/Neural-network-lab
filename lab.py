# import random
# import tensorflow as tf
# import numpy as np
#
# np.random.seed(50)
#
# def init():
#     X = tf.Variable(np.random.uniform(-10, 10), trainable = True)
#     Y = tf.Variable(np.random.uniform(-10, 10), trainable = True)
#     return X, Y
#
# def f(X, Y):
#     return (3*X**4 + 4*X**3 - 12*X**2 + 12*Y**2 - 24*Y)
#
# X, Y = init()
#
# optimizer = tf.optimizers.SGD(learning_rate=0.01, momentum=0.9)
# for epoch in range(1000):
#     optimizer.minimize(lambda: f(X, Y), var_list=[X, Y])
#     print((f(X,Y)).numpy, X.numpy(), Y.numpy(), end="\r")
# print((f(X,Y)).numpy, X.numpy(), Y.numpy(), end="\r")
#

import tensorflow as tf
import numpy as np

# Zainicjalizuj zmienne X i Y
X = tf.Variable(np.random.uniform(-10, 10), trainable=True)
Y = tf.Variable(np.random.uniform(-10, 10), trainable=True)

# Definiuj funkcję f
def f(X, Y):
    return (3*X**4 + 4*X**3 - 12*X**2 + 12*Y**2 - 24*Y)

# Definiuj optymalizator z learning rate i momentum
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.001)

# Pętla trenująca
for epoch in range(1000):
    with tf.GradientTape() as tape:
        loss = f(X, Y)
    gradients = tape.gradient(loss, [X, Y])
    optimizer.apply_gradients(zip(gradients, [X, Y]))
    print("Epoch:", epoch, "Loss:", loss.numpy(), "X:", X.numpy(), "Y:", Y.numpy())
