import numpy as np
import random

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

x = [[0, 0, 1], [0, 0, 1]]
y = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
s = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

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
    # print(j)
    for p in range(2):
        sum1 = 0
        for k in range(3):
            sum1 += s[j][k] * x[p][k]
        sum += (y[p][j] - u[p][j]) * sigmoid_prime(sum1, beta) * x[p][i]
    return sum


def de_Ew(y, u, s, x, i, j, beta):
    sum = 0
    for p in range(2):
        st = 0
        for t in range(9):
            sk = 0
            sl = 0
            for k in range(3):
                sk += s[t][k] * x[p][k]

            for l in range(10):
                sl += w[i][l] * u[p][l]
            st += (y[p][t] - u[p][t]) * sigmoid_prime(sk, beta) * s[t][i] * sigmoid_prime(sl, beta) * u[p][j]
        sum += st
    return sum


def gradient(s_old, w_old, c, y, x, beta):
    s = [[0 for _ in range(3)] for _ in range(9)]
    w = [[0 for _ in range(10)] for _ in range(2)]
    max_difference_s = 0
    max_difference_w = 0

    for j in range(9):
        for i in range(3):
            s[j][i] = s_old[j][i] - c * d_Es(x=x, u=u, y=y, i=i, j=j, s=s_old, beta=beta)
            difference_s = abs(s[j][i] - s_old[j][i])
            if difference_s > max_difference_s:
                max_difference_s = difference_s

    for i in range(2):
        for j in range(10):
            w[i][j] = w_old[i][j] - c * de_Ew(x=x, u=u, y=y, i=i, j=j, s=s_old, beta=beta)
            difference_w = abs(w[i][j] - w_old[i][j])
            if difference_w > max_difference_w:
                max_difference_w = difference_w
    maximum = max([max_difference_s, max_difference_w])
    return s, w, maximum


def autoencoder(u, x, y, w, s, beta):
    for p in range(2):
        for i in range(2):
            for j in range(10):
                x[p][i] += w[i][j] * u[p][j]
            x[p][i] = sigmoid(x=x[p][i], beta=beta)

        for j in range(9):
            for i in range(3):
                y[p][j] += s[j][i] * x[p][i]

            y[p][j] = sigmoid(x=y[p][j], beta=beta)
    return y, x


N = random.uniform(0.5, 10)
w1_r = [random.uniform(-N, N) for _ in range(10)]
w2_r = [random.uniform(-N, N) for _ in range(10)]
w_random = [w1_r, w2_r]
s_random = [[random.uniform(-N, N) for _ in range(3)] for _ in range(9)]

c = 0.8
eps = 0.0001
beta = 1.0

#---dla normalnych wag
# maximum = float('inf')
# while maximum > eps:
#     y, x = autoencoder(u=u, x=x, y=y, w=w, s=s, beta=beta)
#     s, w, maximum = gradient(s_old=s, w_old=w, y=y, c=c, x=x, beta=beta)

#dla losowych wag
w = w_random
s = s_random
maximum = float('inf')
while maximum > eps:
    y, x = autoencoder(u=u, x=x, y=y, w=w, s=s, beta=beta)
    s, w, maximum = gradient(s_old=s, w_old=w, y=y, c=c, x=x, beta=beta)

print(f'dla pierwszego obrazu x:= {x[0]}')
print("Pierwszy obraz:= ")
for i in range(2):
    for j in range(0, 9, 3):
        if i == 1 and j == 0:
            print(f'dla drugiego obrazu x:= {x[1]}')
            print("Drugi obraz:= ")
        print(y[i][j:j + 3])
