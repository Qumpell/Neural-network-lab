import numpy as np


def f(x, beta):
    return 1.0 / (1.0 + np.exp(-beta * x))


def df(x, beta):
    return beta * f(x, beta) * (1.0 - f(x, beta))


def DE_s(y, z, s_old, x, i, beta):
    result = 0
    for p in range(4):
        sm1 = 0
        for k in range(3):
            sm1 += s_old[k] * x[p][k]
        result += (y[p] - z[p]) * df(sm1, beta) * x[p][i]
    return result


def DE_w(y, z, u, s_old, w_old, x, i, j, beta):
    result = 0
    for p in range(4):
        sm1 = 0
        sm2 = 0
        for k in range(3):
            sm1 += s_old[k] * x[p][k]
            sm2 += w_old[i][k] * u[p][k]
        result += (y[p] - z[p]) * df(sm1, beta) * s_old[i] * df(sm2, beta) * u[p][j]
    return result


def calculate_max(s_new, s_old, w_new, w_old):
    max_s = 0.0
    max_w = 0.0
    for i in range(3):
        if abs(s_new[i] - s_old[i]) > max_s:
            max_s = abs(s_new[i] - s_old[i])
        if i < 2:
            for j in range(len(w_new[i])):
                if abs(w_new[i][j] - w_old[i][j]) > max_w:
                    max_w = abs(w_new[i][j])
    return max([max_s, max_w])


def gradient(s_old, w_old, c, y, z, x, beta):
    s_new = [0, 0, 0]
    w_new = [[0, 0, 0], [0, 0, 0]]

    for i in range(3):
        s_new[i] = s_old[i] - c * DE_s(y=y, z=z, s_old=s_old, x=x, i=i, beta=beta)
        if i < 2:
            for j in range(3):
                w_new[i][j] = w_old[i][j] - c * DE_w(y=y, z=z, u=u, s_old=s_old, w_old=w_old, x=x, i=i, j=j, beta=beta)

    return s_new, w_new


def dnn(u, w_old, s_old, z, beta, c, eps):
    y = []
    x = []
    for p in range(4):
        x_i = []
        sum_y = 0
        for i in range(3):
            sm = 0
            for j in range(3):
                if i <= 1:
                    sm += w_old[i][j] * u[p][j]
            xpi = f(sm, beta)
            if i == 2:
                xpi = 1.0
            x_i.append(xpi)
            sum_y += s_old[i] * xpi
        x.append(x_i)
        y.append(f(sum_y, beta))
    s_new, w_new = gradient(s_old=s_old, w_old=w_old, c=c, y=y, z=z, x=x, beta=beta)
    return y, s_new, w_new, w_old, s_old


u = [(0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (0.0, 1.0, 1.0), (1.0, 1.0, 1.0)]
w1 = [[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]
s1 = [0.0, 1.0, 2.0]
beta = [1.0, 2.0, 2.5, 3.0]
z = [0.0, 1.0, 1.0, 0.0]
c = 0.5
eps = 0.0001

y, s_new, w_new, w_old, s_old = dnn(u, w1, s1, z, beta[0], c, eps)
while calculate_max(s_new, s_old, w_old, w_old) > eps:
    y, s_new, w_new, w_old, s_old = dnn(u, w_new, s_new, z, beta[0], c, eps)

print(f's_new:= {s_new}')
print(f'w_new:= {w_new}')
print(f'y:= {y}')
