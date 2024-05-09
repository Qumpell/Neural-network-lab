u1 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
u2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0]
]
u3 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]
u4 = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
u5 = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]
w1 = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
w2 = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 1, 1]
]
w3 = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
w4 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
w = [w1, w2, w3, w4]
u = [u1, u2, u3, u4, u5]


def f(x):
    return 1 if x >= 0 else 0


def cnn(w, u):
    theta = 2.5
    x = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            sm1 = 0
            for ip in range(-1, 2):
                # sm = 0
                for jp in range(-1, 2):
                    try:
                        s = 0
                        if i + ip < 0 or j + jp < 0:
                            sm1 += w[ip + 1][jp + 1] * 0
                        else:
                            sm1 += w[ip + 1][jp + 1] * u[i + ip][j + jp]
                    except IndexError as e:
                        sm1 += 0
                # sm1 += sm
            # x[i][j] = f(sm1) - theta
            # x[i][j] = f(sm1) - theta
            x[i][j] = f(sm1 - theta)
    return x


x = 0
k = 1
for i in range(5):
    for j in range(1):
        # for j in range(4):
        print(f'w[{j + 1}] := {w[j]}')
        print(f'u[{i + 1}] := {u[i]}')
        x = cnn(w[j], u[i])
        print(f'{k} x:=')
        k = k + 1
        for sublist in x:

            out = ""
            for sub in sublist:
                if sub == 1:
                    out = out + " *"
                else:
                    out = out + " 0"
            print(out)
