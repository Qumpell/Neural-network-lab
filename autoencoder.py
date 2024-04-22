import numpy as np


def sigmoid(x, beta):
    return 1 / (1 + np.exp(-beta * x))

def sigmoid_prime(x, beta):
    return sigmoid(x, beta) * (1 - sigmoid(x, beta))

u1 = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]
u2 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
u = [u1, u2]

w1 = [20, 0, 0, 0, 0, 0, 0, 0, 0, -10]
w2 = [0, 0, 20, 0, 0, 0, 0, 0, 0, -10]
w = [w1, w2]
beta = 2.5

x = [[0, 0, 1], [0, 0, 1]]
y = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
s = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# y = s.copy()

def calculate_s_weights(input_vectors):
    for j in range(9):
        for i in range(3):
            if i == 0 or i == 1:
                s[j][i] = 20 * u[i][j]
            elif i == 2:
                s[j][i] = -10
            else:
                continue
    return s


s = calculate_s_weights(s)
# print(s)

def d_Es(y, u, s, x, i, j, beta):
    sum = 0
    for p in range(2):
        # sum +=
        sum1 =0
        for k in range(3):
            sum1 += s[j][k] * x[p][k]
        sum += (y[p][j] - u[p][j]) * sigmoid_prime(sum1, beta) * x[p][i]
    return sum


def de_Ew():
    pass


for p in range(2):
    for i in range(2):
        # x[p][i] = sigmoid(w[i])
        for j in range(10):
            x[p][i] += w[i][j] * u[p][j]
        x[p][i] = sigmoid(x=x[p][i], beta=beta)

    for j in range(9):
        for i in range(3):
            y[p][j] += s[j][i] * x[p][i]

        y[p][j] = sigmoid(x=y[p][j], beta=beta)
    for j in range(9):
        for i in range(3):
            s[j][i] = d_Es(x=x, y=y, i=i, j=j, s=s, beta=beta)
    for i in range(2):
        for j in range(10):
            w[i][j] = de_Ew()


for i in range(2):
    for j in range(0, 9, 3):
        print(y[i][j:j+3])

