import math
c = 0.5
eps = 0.001
beta = 1.0
wNew = [[], []]
sNew = []
wOld = [[0, 1, 2], [0, 1, 2]]
sOld = [0, 1, 2]
u = [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
z = [0, 1, 1, 0]
y = [0, 0, 0, 0]
x = [[0, 0, 1], [0,0,1],[0,0,1],[0,0,1]]

maxW = 0
def f(u, beta):
    return 1.0/(1.0 + math.exp(-beta*u))

def countX(beta):
    for i in range(4):
        x[i][0] = f(wOld[0][0] * u[i][0] + wOld[0][1] * u[i][1] +wOld[0][2] * u[i][2],beta)
        x[i][1] = f(wOld[1][0] * u[i][0] + wOld[1][1] * u[i][1] +wOld[1][2] * u[i][2],beta)
        x[i][2] = 1.0
def countY(beta):
    for i in range(4):
        y[i] = f(sOld[0] * x[i][0] + sOld[1] * x[i][1] + sOld[2] * x[i][2],beta)

def E():
    return (1/2)*sum((y[i]-z[i])**2 for i in range(len(y)))

def Df(u, beta):
    return beta * f(u, beta)* (1.0 - f(u,beta))

def DE_s(beta):
    newDE_s = []
    for e in range(3):
        newDE_s.append(sum((y[i]-z[i]) * Df(sOld[0] * x[i][0] + sOld[1] * x[i][1] + sOld[2] * x[i][2], beta) * x[i][e] for i in range(len(y))))
    return newDE_s

def DE_w(beta):
    newDE_w = []
    for e in range(2):
        newDE_w_inside = []
        for f in range(3):
            newDE_w_inside.append(sum((y[i]-z[i]) *
                Df(sOld[0] * x[i][0] + sOld[1] * x[i][1] + sOld[2] * x[i][2], beta)
                * sOld[e]
                * Df(wOld[e][0] * u[i][0] + wOld[e][1] * u[i][1] + wOld[e][2] * u[i][2],beta) * u[i][f] for i in range(len(y))))
        newDE_w.append(newDE_w_inside)
    return newDE_w

def MaXW(WO,WN):
    diffTable = [abs(WN[i][j] - WO[i][j]) for i in range(len(WO)) for j in range(len(WO[i]))]
    return max(diffTable)


def gradient(sNew, wNew, sOld,wOld,beta,maxW):
    countX(beta)
    countY(beta)
    DFs = DE_s(beta)
    DFs = [c*i for i in DFs]
    sNew.clear()
    sNew.extend([sOld[i] - DFs[i] for i in range(len(sOld))])
    DFw = DE_w(beta)
    DFw = [[c*j for j in i] for i in DFw]
    wNew.clear()
    wNew.extend([[wOld[i][j] - DFw[i][j] for j in range(len(wOld[i]))] for i in range(len(wOld))])
    maxW = MaXW(wOld, wNew)

licznik = 1
gradient(sNew, wNew,sOld,wOld,beta,maxW)
# print(f'Si new: {sNew} ')
# print(f'Wij new: {wNew} ')
# print(f'y:= : {y} ')
while(max(maxW,max([abs(sNew[i] - sOld[i]) for i in range(len(sOld))]))) > eps:
    # zz = (max(maxW,max([abs(sNew[i] - sOld[i]) for i in range(len(sOld))])))
    # print(f'zz: {zz}')
    # print(f'maxW: {maxW}')
    # print(max([abs(sNew[i] - sOld[i]) for i in range(len(sOld))]))

    sOld = list(sNew)
    wOld = list(wNew)
    # print(sNew,wNew)
    gradient(sNew,wNew,sOld,wOld,beta,maxW)
    # print(f'zz: {zz}')
    # print(f'maxW: {maxW}')
    # print(max([abs(sNew[i] - sOld[i]) for i in range(len(sOld))]))
    licznik += 1

print(f'Si new: {sNew} ')
print(f'Wij new: {wNew} ')
print(f'y:= : {y} ')
