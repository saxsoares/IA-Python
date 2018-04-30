import math
import random
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pylab as plt
#import numpy as np


def plot3D(sol, fitness, j):
    # Plot the surface.
    ax.cla()
    ax.view_init(30, j*10)
    surf = ax.plot_surface(Xs, Ys, Zs, cmap=cm.coolwarm,
                           linewidth=1, antialiased=False, alpha=0.5)
    
    ax.scatter(sol[0], sol[1], fitness, c='r', s=50)
    plt.draw()    
    plt.pause(0.00000001)

def rosenbrock (x):
  fitness = 0
  for i in range(len(x)-1):
    fitness += 100*((x[i]**2)-x[i+1])**2+(1-x[i])**2
  return fitness


def Vizinho (S, li, ls):
    for i in range(len(S)):
        S[i] = S[i] + random.uniform(-2, 2)
        if (S[i] < li[i]): S[i] = li[i]
        elif (S[i] > ls[i]): S[i] = ls[i]
    return S

def sa(S0, fun, li, ls, maxIter, alfa, T0):
   #inserir verificacoes de variaveis
   S = list(S0)
   T = T0
   j = 0

   SMelhor = list(S)
   FMelhor = fun(S)
   curvaFit = [FMelhor]
   
   plot3D(SMelhor, FMelhor, 0)
   
   while (j < maxIter):
       Si = Vizinho (S, li, ls)
       deltaFi = fun(Si) - fun(S)
       if ((deltaFi <=0 ) or (random.uniform(0, 1) < math.exp(-abs(deltaFi)/T))):
           S = list(Si)
           if (fun(S) < FMelhor):
                  SMelhor = list(S)
                  FMelhor = fun(S)
                  curvaFit.append(FMelhor)
#                  plotAG_2D(SMelhor, FMelhor, curvaFit, li, ls)
                  plot3D(SMelhor, FMelhor, j)
                  print (" Iter:", j, "  Novo melhor f(", SMelhor, ") =", FMelhor)

       T = T * alfa
       j = j + 1

   return {'solucao': SMelhor, 'valor': FMelhor}



#generate 3d data
Xs = np.arange(-15, 15, 0.1)
Ys = np.arange(-15, 15, 0.1)
Xs, Ys = np.meshgrid(Xs, Ys)
Zs = Xs.copy()
for i in range(len(Xs)):
    for j in range(len(Xs[0])):
        Zs[i,j] = rosenbrock( [Xs[i,j], Ys[i,j]] )
        
fig = plt.figure()
ax = fig.gca(projection='3d')

resultado = sa([-15,15], rosenbrock, [-15, -15], [15, 15], 5000, 0.99, 50)

plot3D(resultado['solucao'], resultado ['valor'], 10)



