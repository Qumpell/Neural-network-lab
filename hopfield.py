import random as rd
z_p  = [
    0, 1, 1, 1, 0,
    0, 1, 0, 1, 0,
    0, 1, 0, 1, 0,
    0, 1, 0, 1, 0,
    0, 1, 1, 1, 0
]
z  = [
    0, 0, 0, 0, 0,
    0, 1, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0
]
# z  = [
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0]
# ]

def give_xi():
    if rd.randint(0, 1) == 0:
        return 0
    else:
        return 1

def calculate_new_xi_based_on_ui(ui, xi):
    if ui < 0:
        return 0
    elif ui == 0:
        return xi
    else:
        return 1


c = [[ 0 for _ in range(25) ] for _ in range(25)]
w = [[ 0 for _ in range(25) ] for _ in range(25)]
theta = [0 for _ in range(25)]
for i in range(25):
    for j in range(25):
        if i == j:
            c[i][j] = 0
        else:
            c[i][j] = (z[i] -1/2) *(z[j] - 1/2)
        w[i][j] = 2 * c[i][j]
        theta[i] += c[i][j]

x = [0 for _ in range(25)]
for i in range(25):
    x[i] = give_xi()

u = [0 for _ in range(25)]


def beautify_print(x, t):
    print(f'x(t) = x({t}):')
    for i in range(0, 25, 5):
        for e in x[i:i+5]:
            if e == 0:
                print(f'-', end="")
            else:
                print(f'*', end="")
        print()

def calcuate_ui_and(x, w, u):
    for i in range(25):
        for j in range(25):
            u[i] += (w[i][j] * x[j])
    return u


for t in range(2):
    beautify_print(x, t)
    u = calcuate_ui_and(x, w, u)
    for i in range(25):
        u[i] = u[i] - theta[i]
        x[i] = calculate_new_xi_based_on_ui(u[i], x[i])



