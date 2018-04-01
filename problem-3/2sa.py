import sys
import random
import math

def objFun(x):
    return 10*math.sin(0.3*x)*math.sin(1.3*x**2)+0.00001*x**4+0.2*x+80

def Vizinho(S, li, ls, passo):
    Si = S + random.uniform(-passo, passo)
    if Si < li: Si = li
    elif Si > ls: Si = ls
    return Si

def sa(fun, S0, li, ls, maxI, alfa, T0):
    S = S0
    T = T0
    j = 0
    melhorI = 0
    melhorS = S
    melhorV = fun(S)
    passo = (ls - li)/10.0
    random.seed(1)
    while j < maxI:
        Si = Vizinho(S, li, ls, passo)
        delta = fun(Si) - fun(S)
        if delta <= 0 or random.uniform(0,1) < math.exp(-delta/T):
            S = Si
            if fun(S) < melhorV:
                melhorS = S
                melhorV = fun(S)
                melhorI = j
        T = T * alfa
        j = j + 1
    return [melhorS, melhorV]

config = sys.stdin.readline().strip().split(' ')
config = [float(val) for val in config]
result = sa(objFun, *config)

print "%.5f %.5f" % (result[0], result[1])
