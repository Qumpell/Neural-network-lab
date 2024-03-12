import numpy as np

def f(x, beta):
    return 1 / (1 + np.exp(-beta * x))

def dnn(u, w, s, beta):
    y = []
    for p in range(4):
        sm = 0
        for i in range(3):
            xpi = 0
            for j in range(3):
                if i <= 1:
                    xpi += w[i][j] * u[p][j]
            sm += s[i] * f(xpi, beta)
        y.append(f(sm, beta))
    return y

u = [(0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
w1 = [[2.0, 2.0, -3.0],[2.0, 2.0, -1.0]]
s1 = [-2.0, 2.0, -1.0]
w2 = [[0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]
s2 = [0.0, 1.0, 2.0]
beta = [1.0, 2.0, 2.5, 3.0]

for b in beta:
    print(dnn(u,w1,s1,b))

print("2:=")
for b in beta:
    print(dnn(u, w2, s2, b))

