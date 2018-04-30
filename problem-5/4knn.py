import math
import random
import sys
from collections import Counter

def knn(new, ents, resps, k):
    dists = []
    for i in range(len(ents)):
        dists.append(
            math.sqrt(sum([(n-e)**2 for n,e in zip(new, ents[i])]))
        )
    tupla = zip(dists, resps)
    ordem = sorted(tupla, key=lambda k: k[0])[:k]
    valores = [m[1] for m in ordem]
    return Counter(valores).most_common()[0][0]

###################################################################
# Main

# Le a linha com as configuracoes
config = sys.stdin.readline().strip().split(';')

random.seed(int(config[0]))

nDim = int(config[1])
tamTreino = int(config[2])
tamTeste = int(config[3])

cores = ['r', 'b', 'g', 'k', 'm']

dadosTreino = [ [random.uniform(-1.0, 1.0) for i in range(nDim)]  for j in range(tamTreino)]
dadosTeste = [ [random.uniform(-1.5, 1.5) for i in range(nDim)]  for j in range(tamTeste)]

respTreino = [random.choice(cores[:nDim]) for _ in range(tamTreino)]
respTeste =  [random.choice(cores[:nDim]) for _ in range(tamTeste)]

vetK = [1, 3, 5]
erros = []
for valK in vetK:
    estimado = []
    aux = []

    for i in range(tamTeste):
        estimado.append(knn(dadosTeste[i], dadosTreino, respTreino, valK))
        aux.append(estimado[i] == respTeste[i])

    erros.append(float(aux.count(True))/float(tamTeste))

# Saida
for valor in erros:
    print ("%.3f" % valor)
