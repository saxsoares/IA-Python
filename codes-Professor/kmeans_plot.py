# -*- coding: utf-8 -*-
import random
import sys
import math
import matplotlib.pyplot as plt

def plot_dados_grupos(dados, centroides = None, grupos = None, SEQ = float("inf")):
    cores = ['r', 'g', 'b', 'k', 'y', 'c', 'm', 'steelblue', 'greenyellow', 'lightsalmon', 'brown', 'silver', 'goldenrod'] * 10
    cores_grupos = ['k'] * len(dados) if grupos is None else [cores[g] for g in grupos]
    
    plt.cla()
    plt.clf()
    x = [d[0] for d in dados]
    y = [d[1] for d in dados]
    plt.scatter(x, y, color = cores_grupos, s=100)
    if centroides is not None:
        x = [d[0] for d in centroides]
        y = [d[1] for d in centroides]

        plt.scatter(x, y, marker='*', s=800, color='k')
        plt.scatter(x, y, marker='*', s=250, color='yellow')
        plt.scatter(x, y, marker='*', s=100, color=cores)
    plt.title("SEQ=" + str(SEQ))
    plt.pause(1)
    plt.draw()
    #plt.show()
    #plt.show(block=False)

def dist_euc(x, y, D, n):
    return math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))]))

def media_colunas(dados, D, n):
    medias = [0.] * D
    for i in range(n):
        for j in range(D):
            medias[j] += dados[i][j]
    
    for j in range(D):
        medias[j] /= n
    return medias


def kmedias(semente, k, D, n, max_iter, dados):

    random.seed(semente)

    # Gera k centroides aleatorios
    centroides = [[random.random() for _ in range(D)] for _ in range(k)]
    
    # Aloca todos os exemplos para o grupo zero
    grupos = [0] * n
    
    # Aloca a lista de distancias
    distancias = [0] * n
    
    # Inicialize a Soma dos Erros Quadrados
    SEQ = float("inf")

    for iter in range(max_iter):
        plot_dados_grupos(dados, centroides, grupos, SEQ)
        
        mudou = False
        
        # Atualiza o grupo de cada um dos exemplos
        for i in range(n):
            # Encontra o centroide mais proximo e pega seu grupo
            distancias[i] = float("inf")
            for j in range(k):
                dist = dist_euc(dados[i], centroides[j], D, n)
                if dist < distancias[i]:
                    distancias[i] = dist
                    novo_grupo = j

            if novo_grupo != grupos[i]:
                mudou = True
                grupos[i] = novo_grupo

        # Finaliza caso nao haja mudanca
        if not mudou: break
                
        # Atualiza os centroides, calculando-se a media de cada grupo
        for j in range(k):
            # Obtem os membros do grupo j=0,...,k-1
            membros_grupo = []
            for i in range(n):
                if grupos[i] == j:
                    membros_grupo.append (dados[i])

            centroides[j] = media_colunas(membros_grupo, D, len(membros_grupo))
            
        # Calcula o SEQ
        SEQ = sum(distancias)

    return SEQ, grupos


##########################################
#
#  MAIN
#
##########################################

# 1, 3, 2, 200, 10
# Le a configuracao de entrada
#semente, k, D, n, max_iter = map(int, sys.stdin.readline().strip().split(';'))
semente, k, D, n, max_iter = map(int, "2;2;2;58;10".strip().split(';'))

random.seed(semente)

# Gera o conjunto de dados aleatoriamente
dados = [[random.random() for _ in range(D)] for _ in range(n)]

#plt.figure()
plot_dados_grupos(dados)

SEQ, grupos = kmedias(semente, k, D, n, max_iter, dados)

print "{:.3f};{}".format(SEQ, grupos)





