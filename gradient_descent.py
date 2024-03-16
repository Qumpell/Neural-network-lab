from random import *
import numpy as np


# -10 10

def DF1_x1(x1, x2, x3):
    return 4 * x1 - 2 * x2 - 2


def DF1_x2(x1, x2, x3):
    return 4 * x2 - 2 * x1 - 2 * x3


def DF1_x3(x1, x2, x3):
    return 2 * x3 - 2 * x2


def DF2_x1(x1, x2):
    return 12 * pow(x1, 3) + 12 * pow(x1, 2) - 24 * x1


def DF2_x2(x1, x2):
    return 24 * x2 - 24


def F1(x1, x2, x3):
    return (2 * (x1 ** 2) + 2 * (x2 ** 2)
            + (x3 ** 2) - 2 * x1 * x2 - 2 * x2 * x3 - 2 * x1 + 3)


def F2(x1, x2):
    return (3 * (x1 ** 4) + 4 * (x1 ** 3) - 12 * (x1 ** 2) +
            12 * (x2 ** 2) - 24 * x2)


def gradient_descent_F1(X, c, eps):
    error = [1000, 1000, 1000]
    x_new = [0, 0, 0]
    x_old = X
    while max(np.absolute(error)) > eps:
        for i in range(3):
            if i == 0:
                x_new[i] = x_old[i] - c * DF1_x1(x_old[0], x_old[1], x_old[2])
            elif i == 1:
                x_new[i] = x_old[i] - c * DF1_x2(x_old[0], x_old[1], x_old[2])
            elif i == 2:
                x_new[i] = x_old[i] - c * DF1_x3(x_old[0], x_old[1], x_old[2])

            error[i] = x_new[i] - x_old[i]
        for i in range(3):
            x_old[i] = x_new[i]

    print(x_new[0], x_new[1], x_new[2], F1(x_new[0], x_new[1], x_new[2]))


def gradient_descent_F2(X, c, eps):
    error = [1000, 1000]
    x_new = [0, 0]
    x_old = X
    while max(np.absolute(error)) > eps:
        for i in range(2):
            if i == 0:
                x_new[i] = x_old[i] - c * DF2_x1(x_old[0], x_old[1])
            elif i == 1:
                x_new[i] = x_old[i] - c * DF2_x2(x_old[0], x_old[1])
            error[i] = x_new[i] - x_old[i]
        for i in range(2):
            x_old[i] = x_new[i]
    print(x_new[0], x_new[1], F2(x_new[0], x_new[1]))


a = randrange(-5, 5)
b = randrange(-5, 5)
c = randrange(-5, 5)
X = [a, b, c]
c = 0.01
eps = 0.0001
X2 = [a, b]
gradient_descent_F1(X, c, eps)
gradient_descent_F2(X2, c, eps)
