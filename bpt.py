import numpy as np


def f(x, beta):
    return 1.0 / (1.0 + np.exp(-beta * x))


def df(x, beta):
    return beta * f(x, beta) * (1.0 - f(x, beta))


def DE_s(y, z, s_old, x, i, beta):
    result = 0
    for p in range(4):
        sm = y[p] - z[p]
        sm1 = np.dot(s_old, x[p])
        result += sm * df(sm1, beta) * x[p][i]
    return result


def DE_w(i, y, s_old, x, u, z, j, w_old, beta):
    result = 0
    for p in range(4):
        sm = y[p] - z[p]
        sm1 = np.dot(s_old, x[p])
        sm2 = np.dot(w_old[i], u[p])
        result += sm * df(sm1, beta) * s_old[i] * df(sm2, beta) * u[p][j]
    return result


def gradient(s, w, y, eps, c, x, z, beta, u):
    s_new = s.copy()
    s_old = np.array([float('inf'), float('inf'), float('inf')])
    w_old = np.array([[float('inf'), float('inf'), float('inf')], [float('inf'), float('inf'), float('inf')]])
    w_new = w.copy()
    while max(np.max(np.abs(s_new - s_old)), np.max(np.abs(w_new - w_old))) > eps:
        s_old = s_new.copy()
        w_old = w_new.copy()
        for i in range(3):
            s_new[i] = s_old[i] - c * DE_s(y, z, s_old, x, i, beta)
            for j in range(2):
                if i <= 1:
                    w_new[i][j] = w_old[i][j] - c * DE_w(i, y, s_old, x, u, z, j, w_old, beta)
    return s_new, w_new


def dnn(u, w, s, z, beta, c, eps):
    y = []
    x = np.array([])
    for p in range(4):
        x_i = []
        smy = 0
        for i in range(3):
            sm = 0
            for j in range(3):
                if i <= 1:
                    sm += w[i][j] * u[p][j]
            xpi = f(sm, beta)
            smy += s[i] * xpi
            x_i.append(xpi)
        x = np.vstack((x, x_i)) if x.size else np.array(x_i)
        y.append(f(smy, beta))
    s, w = gradient(s, w, y, eps, c, x, z, beta, u)

    return y, s, w


u = np.array([(0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (0.0, 1.0, 1.0), (1.0, 1.0, 1.0)])
w1 = np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]])
s1 = np.array([0.0, 1.0, 2.0])
beta = 1.0
z = np.array([0.0, 1.0, 1.0, 0.0])
c = 0.5
eps = 0.0001

for i in range(1):
    y, s1, w1 = dnn(u, w1, s1, z, beta, c, eps)

print(y)
