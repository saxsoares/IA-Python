import sys
import math
import random
from collections import Counter

# Retorna a media das respostas das k entradas mais proximas ao novo_exemplo
# 1) Calcula a distancia euclidiada (sqrt(sum((x - y)^2))) entre novo_exemplo e cada uma das entradas
# 2) Monta uma tupla (distancia, resposta)
# 3) Ordena as tuplas, da menor distancia para a maior
# 4) Pega os valores das k respostas ordenadas
# 5) Calcula a media e retorna o valor

def knn(novo_exemplo, entradas, respostas, k):
    distancias = []
    for i in range(len(entradas)):
        distancias.append(
            math.sqrt(sum([(n-e)**2 for n, e in zip(novo_exemplo, entradas[i])]))
        )
    tupla = zip(distancias, respostas)
    ordem = sorted(tupla, key= lambda k: k[0])[:k]

    valores = [m[1] for m in ordem]
    
    ###### IMPLEMENTE AQUI O RETORNO DA RESPOSTA MAIS FREQUENTE DENTRE OS K VIZINHOS MAIS PROXIMOS
    return Counter(valores).most_common()[0][0]

########################
# Main
########################

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
    contador = []
    estimado = []
    for i in range(tamTeste):
        estimado.append(knn(dadosTeste[i], dadosTreino, respTreino, valK))
        contador.append(estimado[i] == respTeste[i])

    ###### IMPLEMENTE AQUI O CALCULO DA ACURACIA
    erros.append(float(contador.count(True))/float(tamTeste))

# Saida
for valor in erros:
    print ("%.3f" % valor)
