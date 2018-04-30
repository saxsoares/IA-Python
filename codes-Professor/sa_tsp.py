import sys
import random
import math
import matplotlib.pyplot as plt

def cria_mapa (qtd):
    return [ [random.random(), random.random()] for i in range(qtd) ]

# mapa = cria_mapa(5)
# print (mapa)
    
def desenha_mapa(mapa, ordem, custo=float('inf')):
    plt.cla()
    plt.clf()
    for pos in range(len(ordem)-1):
        x = [mapa[ordem[pos]][0], mapa[ ordem[pos+1]] [0]]
        y = [mapa[ordem[pos]][1], mapa[ ordem[pos+1]] [1]]
        plt.plot (x, y, "ro-", linewidth=5)
        
    x = [mapa[ ordem[0] ][0], mapa[ ordem[-1] ][0]]
    y = [mapa[ ordem[0] ][1], mapa[ ordem[-1] ][1]]        
    plt.plot (x, y, "ro-", linewidth=5)
    plt.title("Custo=" + str(custo))
    plt.draw()
    plt.show()    
    plt.pause(0.000001)

# desenha_mapa(mapa, range(len(mapa)))    
   

def calc_dist (mapa, qtd_cidades):
    matDist = [ [0] * qtd_cidades for i in range(qtd_cidades)]
    for i in range(qtd_cidades):
        for j in range(i):
            d = math.sqrt((mapa[i][0] - mapa[j][0])**2 + (mapa[i][1] - mapa[j][1])**2)
            matDist [i][j] = d
            matDist [j][i] = d      
    return matDist
    
# matDist = calc_dist(mapa, len(mapa))

def objfun(sol, matDist):
    custo = 0
    for i in range(len(sol)-1):
        custo = custo +  matDist[ sol[i] ][ sol[i+1] ]
    custo = custo +  matDist[ sol[0] ][ sol[-1] ]
    return custo

    
def Vizinho (S, maxTrocas):
    Si = list(S)
    for i in range(maxTrocas):
        troca = random.sample(range(len(Si)), 2)
        Si[troca[0]], Si[troca[1]] = Si[troca[1]], Si[troca[0]]
    return Si

#Vizinho (range(10), 2)
    
    
def sa (fun, mapa, matDist, S0, maxIter, alfa, T0, maxTrocas):
    S=list(S0)
    melhorSol = S
    melhorVal = fun(S, matDist)
    # melhorIter = 0
    T=T0
    j = 0
       
    while (j < maxIter):
        Si = Vizinho (S, maxTrocas)
        delta = fun(Si, matDist) - fun(S, matDist)
        if delta <= 0 or random.uniform(0, 1) < math.exp(-delta/T):
            S = list(Si)
            # print "Nova sol=", S, "valor=", fun(S)
            if fun(S, matDist) < melhorVal:
                melhorVal = fun(S, matDist)
                melhorSol = list(S)
                desenha_mapa(mapa, S, melhorVal)
                
                # melhorIter = j
                print (">>> Nova melhorSol=", S, "melhorVal=", melhorVal)

        T = T * alfa
        j = j + 1
        # print "Temp=", T
        
    return [melhorSol, melhorVal]
    

########################
# Main
########################
         

random.seed(1)

qtd_cidades = 50
mapa = cria_mapa(qtd_cidades)
matDist = calc_dist (mapa, qtd_cidades)
S0 = list(range(qtd_cidades))
random.shuffle(S0)
resultado = sa(objfun, mapa, matDist, S0, 100000, 0.99, 10, 2)


