# carrega e mistura
import math
import random
import matplotlib.pyplot as plt # required for plotting
from mpl_toolkits.mplot3d import Axes3D


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

    print " ".join([m[2] for m in melhores]),
    valores = [m[1] for m in melhores]
    return float(sum(valores))/len(valores)


    
random.seed(1)

# Funcao objetivo
objfun = lambda x: x[0]**2 + x[1]

nDim = 2
tamTreino = 10
tamTeste = 5
dadosTreino = [ [random.uniform(-1.0, 1.0) for i in range(nDim)]  for j in range(tamTreino)]
dadosTeste = [ [random.uniform(-1.5, 1.5) for i in range(nDim)]  for j in range(tamTeste)]

respTreino = [ objfun(variaveis) for variaveis in dadosTreino ]
respTeste = [ objfun(variaveis) for variaveis in dadosTeste ]

fig=plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

for i in range(tamTreino):
    ax.scatter(dadosTreino[i][0], dadosTreino[i][1], respTreino[i], c='steelblue', marker='o', s=50)
    ax.text(dadosTreino[i][0], dadosTreino[i][1], respTreino[i], str(i), fontsize=14, color="whitesmoke")
    ax.text(dadosTreino[i][0]-0.005, dadosTreino[i][1]+0.005, respTreino[i], str(i), fontsize=14)


for i in range(tamTeste):
    ax.scatter(dadosTeste[i][0], dadosTeste[i][1], respTeste[i], c='darkorange', marker='o', s=50)
    ax.text(dadosTeste[i][0], dadosTeste[i][1], respTeste[i], str(i), fontsize=14, color="whitesmoke")
    ax.text(dadosTeste[i][0]-0.005, dadosTeste[i][1]+0.005, respTeste[i], str(i), fontsize=14)
plt.draw()
#plt.show()


plt.figure(2)
plt.plot( range(tamTeste), respTeste, 'o-', markersize=10, label='Original' )

vetK = [1, 2, 3]
for valK in vetK:
    erros = []
    estimado = []
    
    print "\n\nTreino: azul    Teste: laranja"
    for i in range(tamTeste):        
        print "Os k=" + str(valK) + " pontos mais proximos do id=" + str(i) + " sao:",
        estimado.append(knn(dadosTeste[i], dadosTreino, respTreino, valK))
        erros.append(abs(estimado[i] - respTeste[i]))
        print "  Real: %.3f   Estimado: %.3f    Erro:  %.3f" % (respTeste[i], estimado[-1], erros[-1])

    erroMedio = float(sum(erros))/len(erros)
    print "Erro medio=", erroMedio, "\n\n"
    
    #print (erros)
    
    
    plt.plot( range(tamTeste), estimado, 'o-', markersize=10, label='k='+ str(valK) )
# plt.title("K = " + str(valK) + " erroMedio=" + str(erroMedio))
plt.legend(['Original'] + ['k='+str(valK) for valK in vetK])
plt.draw()
plt.show()


