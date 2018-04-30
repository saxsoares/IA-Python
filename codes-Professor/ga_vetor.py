import random
import math

import pylab as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pylab as plt


def plot3D(pop, fitness, j):
    # Plot the surface.
    ax.cla()
    ax.view_init(30, j*10)
    surf = ax.plot_surface(Xs, Ys, Zs, cmap=cm.coolwarm,
                           linewidth=1, antialiased=False, alpha=0.3)

    pop = np.array(pop)
    ax.scatter(pop[:,0], pop[:, 1], fitness, c='r', s=50)    
#    for i in range(len(pop)):
#        ax.scatter(pop[i][0], pop[i][1], fitness[i], c='r', s=50)
    plt.draw()    
    plt.pause(0.00000001)
    
def plotAG_2D(pop, fitness, curvaFit, valMin, valMax):
	tab = np.array(pop)
	plt.clf()
	
	plt.subplot(211)
	plt.scatter(tab[:,0], tab[:,1], 50) #np.array(fitness)+abs(min(fitness))*2)
	plt.ylabel('y=f(x)')
	plt.xlabel('x')
	plt.xlim(valMin[0], valMax[0])
	plt.ylim(valMin[1], valMax[1])
	
	plt.subplot(212)
	plt.plot(curvaFit, 'r--')
	plt.ylabel('fitness')
	plt.xlabel('geracoes')
	plt.yscale('log')
#	plt.draw()
	plt.pause(1e-8)
#	time.sleep(0.05)



def rosenbrock (x):
  fitness = 0
  for i in range(len(x)-1):
    fitness += 100*((x[i]**2)-x[i+1])**2+(1-x[i])**2
  return fitness

def cria_ind (nDim, valMin, valMax):
#    ind = []
#    for i in xrange(nDim):
#        ind.append(r.uniform(valMin, valMax)
    return [ random.uniform(valMin[i], valMax[i]) for i in range(nDim)]

#cria_ind (3, 0.0, 3.0)

def cria_pop (nDim, tamPop, valMin, valMax):
    return [cria_ind (nDim, valMin, valMax) for qtd in range(tamPop)]

#pop = cria_pop (3, 10, 0.0, 3.0)
#print pop
   
def mutacao (ind, probMut):
    for i in range(len(ind)):
        if (random.uniform(0, 1) < probMut):
            ind[i] = ind[i] + random.uniform(-2, 2)
    return ind

#mutacao(0.5, 0.9)

def cruzamento (ind1, ind2):
    novo_ind = list(ind1)
    for i in range(len(ind1)):
        (ind1[i] + ind2[i])/2
    return novo_ind

#cruzamento (0.0, 1.0)

def seleciona (pop):
    return pop[random.randint(0, len(pop)-1)]  #importante o -1

    
def torneio (fitness, tamanho):
    opcoes = list(range(len(fitness)))
    competidores = random.sample(opcoes, tamanho)
    fit = [fitness[idx] for idx in competidores]
    v1 = competidores[fit.index(min(fit))]
    
    opcoes.remove(v1)
    competidores = random.sample(opcoes, tamanho)
    fit = [fitness[idx] for idx in competidores]
    v2 = competidores[fit.index(min(fit))]
    
    return v1, v2
    
#seleciona(pop)

def ga(fun, nDim, valMin, valMax, tamPop, tamTorneio, probMut, porcCr, nGeracoes):
    pop = cria_pop (nDim, tamPop, valMin, valMax)
    fitness = [fun(indiv) for indiv in pop]
    curvaFit = [min(fitness)]

    for ger in range(nGeracoes):        
        for cruzamentos in range( int(tamPop*porcCr) ):
            #pai1 = seleciona(pop)
            #pai2 = seleciona (pop)
            vencedor1, vencedor2 = torneio(fitness, tamTorneio)

            pai1 = pop[vencedor1]
            pai2 = pop[vencedor2]
            filho = cruzamento (pai1, pai2)
            filho = mutacao (filho, probMut)

            #inserir na pop
            pop.append(filho)
            fitness.append(fun(filho))

        #somente os melhores sobrevivem
        #sorted(fitness)
        ordem = sorted(range(len(fitness)), key=lambda k: fitness[k], reverse=False)
        #[fitness[idx] for idx in ordem]

        #selecionar os tamPop melhores
        fitness.sort(reverse=False)
        fitness = fitness [:tamPop]
        curvaFit.append(fitness[0])
        
        pop = [pop[idx] for idx in ordem] [:tamPop]
        
        #if curvaFit[-1] != curvaFit[-2]:
        if True:
            print ("Ger:", ger, " Melhor sol=", pop[0], "  fit=", fitness[0], "  pior sol=", pop[tamPop-1]            )
            #plotAG_2D(pop, fitness, curvaFit, valMin, valMax)
            plot3D(pop, fitness, ger)

        
        #print sum(fitness)/len(fitness)
    pop[0]


#generate 3d data

li = -20
ls = 20
Xs = np.arange(li, ls, 0.1)
Ys = np.arange(li, ls, 0.1)
Xs, Ys = np.meshgrid(Xs, Ys)
Zs = Xs.copy()
for i in range(len(Xs)):
    for j in range(len(Xs[0])):
        Zs[i,j] = rosenbrock( [Xs[i,j], Ys[i,j]] )
        
fig = plt.figure()
ax = fig.gca(projection='3d')

ga(rosenbrock, 2, [li, li], [ls, ls], 100, 3, 0.01, 0.1, 1000)

