from numpy import dot


def f(x):
    if x < 0:
        return 0
    else:
        return 1


def notOperation(u1):
    u = [u1, 1]
    w = [-2, 1]
    return f(dot(u, w))


def andOperation(u1, u2):
    u = [u1, u2, 1]
    w = [2, 2, -3]
    return f(dot(u, w))


def nandOperation(u1, u2):
    u = [u1, u2, 1]
    w = [-2, -2, 3]
    return f(dot(u, w))


def orOperation(u1, u2):
    u = [u1, u2, 1]
    w = [1, 1, -0.5]
    return f(dot(u, w))


print(notOperation(1))
print(andOperation(1, 1))
print(nandOperation(1, 1))
print(orOperation(0, 0))
print(orOperation(0, 1))
print(orOperation(1, 0))
print(orOperation(1, 1))
