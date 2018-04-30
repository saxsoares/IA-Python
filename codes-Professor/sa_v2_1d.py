
# -*- coding: utf-8 -*-
#simulated annealing

#Pseudo-Código Simulated Annealing
#Inicio
#/* Entradas do Algoritmo */
#Ler (S0, FUN, LI, LS, MAXITER, MAXVIZ, ALFA, T0)
#/* Inicialização das variáveis */
#S = S0
#T = T0
#j = 1
#/*Loop principal – Verifica se foram atendidas as condições de termino do algoritmo*/
#Repita
#
#    i = 1
#    nSucesso = 0
#    /*Loop Interno – Realização de perturbação em uma iteração*/
#    Repita
#
#        Si = Perturba(S)
#        ∆Fi = f(Si) – f(S)
#        /*Teste de aceitação de uma nova solução*/
#        Se (∆fi ≤ 0) ou (exp(-∆fi/T) > Randomiza()) então
#
#            S= Si
#            nSucesso = nSucesso + 1
#
#        Fim-se
#        i = i + 1
#
#    Até (nSucesso ≥ L) ou (i > P)
#    /*Actualização da Temperatura*/
#    T = α.T
#    /*Actualização do Contador de iterações*/
#    j = j + 1
#
#Até (nSucesso = 0) ou (j > M)
#/*Saída do Algoritmo*/
#Imprima(S)
#

import random
import math


import matplotlib.pyplot as plt
import random as r
import numpy as np
import time

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def plot_1D(S, val, melhorSol, melhorVal, curve, valcurve, curvaFit):
    plt.figure(1)
    plt.clf()
    plt.cla()

    plt.subplot(211)
    plt.plot(curve, valcurve, 'k')
    plt.plot(S, val, 'ro', markersize=10, markeredgewidth = 2)
    plt.plot(melhorSol, melhorVal, 'r', marker='x', markersize=15,  linewidth = 10, markeredgewidth = 8)
    plt.plot(melhorSol, melhorVal, 'w', marker='x', markersize=15,  linewidth = 10, markeredgewidth = 3)
    plt.ylabel('y=f(x)')
    plt.xlabel('x')

    plt.subplot(212)
    plt.plot(curvaFit, 'r--')
    plt.ylabel('f(x)')
    plt.xlabel('iteracoes')

    plt.draw()
    plt.pause(1e-8)

def objfun(x):
    return 10 * math.sin(0.3 * x) * math.sin (1.3 * x**2) + 0.00001 * x**4 + 0.2*x + 80

def Vizinho (S, li, ls, passo):
    Si = S + random.uniform(-passo, passo)
    if (Si < li): 
        Si = li
    elif (Si > ls): 
        Si = ls
    return Si

def sa (S0, fun, li, ls, maxIter, maxViz, alfa, T0):
    S=S0
    melhorSol = S
    melhorVal = fun(S)
    melhorIter = 0
    passo = (ls-li)/10.0
    passo = 10
    T=T0
    j = 0
    
    curvaFit = [melhorVal]
    curve = np.arange(li, ls, 0.01)
    valcurve = [fun(curve[i])  for i in xrange(len(curve))]
    
    while (j < maxIter):
        Si = Vizinho (S, li, ls, passo)
       	#plot_1D(Si, fun(Si), curve, valcurve, curvaFit)
        plot_1D(Si, fun(Si), melhorSol, melhorVal, curve, valcurve, curvaFit)

        delta = fun(Si) - fun(S)
        if delta <= 0 or random.uniform(0, 1) < math.exp(-delta/T):
            S = Si
#            print "Nova sol=", S, "valor=", fun(S)
            if fun(S) < melhorVal:
                melhorVal = fun(S)
                melhorSol = S
                melhorIter = j
                print ">>> Nova melhorSol=", S, "melhorVal=", melhorVal

        curvaFit.append(melhorVal)
        T = T * alfa
        j = j + 1
#        print "Temp=", T

        
    return [melhorSol, melhorVal, melhorIter]
    
print sa (30, objfun, -50, 50, 30, 1, 0.999, 1000)

# sa(2, calc, -25, 25, 433, 1, 0.92, 663)












