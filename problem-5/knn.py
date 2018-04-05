import math
import random
#import matplotlib.pyplot as plt

# Retorna a media das respostas das k entradas mais proximas ao novo_exemplo
# 1) Calcula a distancia euclidiada (sqrt(sum((x - y)^2))) entre novo_exemplo e cada uma das entradas
# 2) Monta uma tupla (distancia, resposta)
# 3) Ordena as tuplas, da menor distancia para a maior
# 4) Pega os valores das k respostas ordenadas
# 5) Calcula a media e retorna o valor

def knn(novo_exemplo, entradas, respostas, k):
    melhores =  sorted(
                        [
                         [
                             math.sqrt(
                                 sum(
                                  [(n - e)**2 for n, e in zip(novo_exemplo, entradas[j])]   # Calculo da distancia euclidiana entre dois vetores
                                 )
                             ), respostas[j], "id="+str(j)
                         ] for j in range(len(entradas))
                        ],
                        key=lambda tupla: tupla[0]
                )[:k]

    valores = [m[1] for m in melhores]
    # return float(sum(valores))/len(valores)
    ###### IMPLEMENTE AQUI O RETORNO DA RESPOSTA MAIS FREQUENTE DENTRE OS K VIZINHOS MAIS PROXIMOS


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
for valK in vetK:
    erros = []
    estimado = []
    
    for i in range(tamTeste):
        estimado.append(knn(dadosTeste[i], dadosTreino, respTreino, valK))
        #erros.append(abs(estimado[i] - respTeste[i]))

    #erroMedio = sum(erros)/float(len(erros))
    ###### IMPLEMENTE AQUI O CALCULO DA ACURACIA
    

# Saida
for valor in erros:
    print ("%.3f" % valor)


# Desenha os conjuntos de dados
#plt.figure()
#
#for i in range(tamTreino):
#    plt.plot( dadosTreino[i][0], dadosTreino[i][1], 'x', markersize=10, color = respTreino[i], mew=3)
#    plt.text(dadosTreino[i][0], dadosTreino[i][1], str(i), fontsize=14, color="whitesmoke")
#    plt.text(dadosTreino[i][0]-0.005, dadosTreino[i][1]+0.005, str(i), fontsize=14)
#
#for i in range(tamTeste):
#    plt.plot( dadosTeste[i][0], dadosTeste[i][1], 'o', markersize=10, color = respTeste[i])
#    plt.text(dadosTeste[i][0], dadosTeste[i][1], str(i), fontsize=14, color="whitesmoke")
#    plt.text(dadosTeste[i][0]-0.005, dadosTeste[i][1]+0.005, str(i), fontsize=14)
#
#plt.draw()
#plt.show()

