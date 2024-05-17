import numpy as np
#
# z0_img = [
#     [-1, -1, -1, -1, -1],
#     [-1, 1, 1, 1, -1],
#     [-1, 1, -1, 1, -1],
#     [-1, 1, 1, 1, -1],
#     [-1, -1, -1, -1, -1]
# ]
# z1_img = [
#     [-1, -1, -1, -1, -1],
#     [-1, 1, 1, -1, -1],
#     [-1, -1, 1, -1, -1],
#     [-1, -1, 1, -1, -1],
#     [-1, -1, -1, -1, -1]
# ]
z1 = [-1, -1, -1, -1, -1,
      -1, 1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, -1, -1, -1]

z0 = [-1, -1, -1, -1, -1,
      -1, 1, 1, 1, -1,
      -1, 1, -1, 1, -1,
      -1, 1, 1, 1, -1,
      -1, -1, -1, -1, -1]

u0p = [-1, 1, 1, 1, -1,
      -1, 1, -1, 1, -1,
      -1, 1, -1, 1, -1,
      -1, 1, 1, 1, -1,
      -1, -1, -1, -1, -1]

u1p = [-1, -1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, 1, -1, -1,
      -1, -1, -1, -1, -1]


w = [[0.0 for _ in range(25)] for _ in range(25)]
#
# z0 = sum(z0_img, [])
# z1 = sum(z1_img, [])

u0 = z0
u1 = z1

for i in range(25):
    for j in range(25):
        w[i][j] = 1/25 * (z0[i] * z0[j]) + 1/25 * (z1[i] * z1[j])


def beatify_print(result):
    for i in range(0, 25, 5):
        tmp = result[i:i+5]
        for j in tmp:
            if j == 1:
                print("*", end="")
            else:
                print("-", end='')
        print()
    print("--------------")

def sgn(x):
    return 1 if x >= 0 else -1

def calculate_final_result(w, u):
    y = [0 for _ in range(25)]
    final_result = []
    for i in range(25):
        sum = 0
        for j in range(25):
               sum += w[i][j]*u[j]
        y[i] = sum

        # if y[i] <0:
        final_result.append(sgn(y[i]))
    return final_result

w1 =  calculate_final_result(w, u0)
w2 = calculate_final_result(w, u1)
w1p = calculate_final_result(w, u0p)
w2p = calculate_final_result(w, u1p)
# print(w1, w2)
beatify_print(w1)
beatify_print(w2)
beatify_print(w1p)
beatify_print(w2p)

