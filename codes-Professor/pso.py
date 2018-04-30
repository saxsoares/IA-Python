#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:39:35 2018

@author: vmelo
"""

# Particulaenxame.py
# python 3.4.3
# demo of Particula enxame optimization (PSO)
# PSOs Rastrigin's function

import random
# import math    # cos() for Rastrigin
import copy    # array-copying convenience
import sys     # max float

# ------------------------------------

  
def rosenbrock (x):
  valor = 0
  for i in range(len(x)-1):
    valor += 100*((x[i]**2)-x[i+1])**2+(1-x[i])**2
  return valor

# ------------------------------------

class Particula:
  def __init__(self, objfun, nDim, valMin, valMax, velocMin, velocMax):
    self.posicao = [ random.uniform(valMin, valMax) for i in range(nDim) ]
    self.velocidade = [ random.uniform(velocMin, velocMax) for i in range(nDim) ]
    self.melhorPosicaoParticula = list(self.posicao) 
    
    self.fx = objfun(self.posicao) # curr fxr
    self.melhorfxParticula = self.fx # best fxr

def PSO(objfun, maxIter, n, nDim, valMin, valMax, velocMin, velocMax):
  # create n random Particulas
  enxame = [Particula(objfun, nDim, valMin, valMax, velocMin, velocMax) for i in range(n)] 

  melhorPosicaoEnxame = None
  melhorFxEnxame = float("inf")
  for i in range(n): # check each Particula
    if enxame[i].fx < melhorFxEnxame:
      melhorFxEnxame = enxame[i].fx
      melhorPosicaoEnxame = list(enxame[i].posicao) 

  iter = 0
  w = 0.729    # inertia
  c1 = 1.49445 # cognitive (Particula)
  c2 = 1.49445 # social (enxame)

  for iter in range(maxIter):
    
    if iter % 10 == 0 and iter > 1:
      print("iter = " + str(iter) +
        " Melhor fx = %e" % melhorFxEnxame)

    for i in range(n): # process each Particula
      
      # compute new velocidade of curr Particula
      for k in range(nDim):
        r1 = random.random()    # randomizations
        r2 = random.random()
    
        enxame[i].velocidade[k] = ( (w * enxame[i].velocidade[k]) +
          (c1 * r1 * (enxame[i].melhorPosicaoParticula[k] -
          enxame[i].posicao[k])) +  
          (c2 * r2 * (melhorPosicaoEnxame[k] -
          enxame[i].posicao[k])) )  

        if enxame[i].velocidade[k] < velocMin:
          enxame[i].velocidade[k] = velocMin
        elif enxame[i].velocidade[k] > velocMax:
          enxame[i].velocidade[k] = velocMax

        enxame[i].posicao[k] += enxame[i].velocidade[k]
        
        if enxame[i].posicao[k] < valMin:
          enxame[i].posicao[k] = valMin
        elif enxame[i].posicao[k] > valMax:
          enxame[i].posicao[k] = valMax
  
      # compute fxr of new posicao
      enxame[i].fx = objfun(enxame[i].posicao)

      # is new posicao a new best for the Particula?
      if enxame[i].fx < enxame[i].melhorfxParticula:
        enxame[i].melhorfxParticula = enxame[i].fx
        enxame[i].melhorPosicaoParticula = list(enxame[i].posicao)

      # is new posicao a new best overall?
      if enxame[i].fx < melhorFxEnxame:
        melhorFxEnxame = enxame[i].fx
        melhorPosicaoEnxame = list(enxame[i].posicao)
    
  # while
  return melhorPosicaoEnxame
# end PSO



random.seed(1)

nDim = 10
nParticulas = 50
maxIter = 1000

melhorPosicao = PSO(rosenbrock, maxIter, nParticulas, nDim, -10.0, 10.0, -1.0, 1.0)

print("\nMelhor solucao encontrada: ")
print (["%.3f" % v for v in melhorPosicao])
fx = rosenbrock(melhorPosicao)
print("  fx = %.6f" % fx)
