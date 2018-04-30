# coding=utf-8
# perceptron
# Ajuste de curva: curve fitting
# Toda equacao na forma y = mx + q é chamada equacao reduzida da reta, 
# em que m é o coeficiente angular e q a ordenada do ponto n qual a reta cruza o eixo Oy.

import matplotlib.pyplot as plt
import random

random.seed(10)

qtd_pontos = 10
vet = sorted([ random.random() for _ in range(qtd_pontos)])
vet= [[v] for v in vet]
fx = [ v[0] + random.uniform(-10, 10) for v in vet]

plt.cla()
plt.clf()
plt.scatter(vet, fx)
plt.ylabel('y=f(x)')
plt.xlabel('x')
plt.draw()
#plt.show()


def ativacao(x): return x

dados = [[1] + v for v in vet]

nDados = len(dados)
nDim = len(dados[0])
pesos = [random.uniform(-100, 100) for _ in range(nDim)]
erros = []
erros_float = []
alfa = 0.9
max_epocas = 10


for epoca in range(max_epocas):
    soma_erros = 0
    soma_erros_float = 0.0
    predicao = []
    for i in range(nDados):
        entrada = dados[i]
        saida = fx[i]
        entrada_pesos = list(zip(entrada, pesos))
        print "entradas: " 
        print entrada
        print "pesos: " 
        print pesos
        print entrada_pesos
        saida_calculada = sum([e*p for e,p in entrada_pesos])
        predicao.append(saida_calculada)
        erro = saida - ativacao(saida_calculada)
        #erro = saida - saida_calculada
        pesos = [p + alfa * erro * e for e,p in entrada_pesos]
        
        soma_erros += abs(erro)
        #soma_erros += abs(erro)
        soma_erros_float += abs(saida - ativacao(saida_calculada))
    erros.append(soma_erros)
    erros_float.append(soma_erros_float)
    
    plt.cla()
    plt.clf()
    plt.scatter(vet, fx)
    plt.plot(vet, predicao, '-')
    plt.ylabel('y=f(x)')
    plt.xlabel('x')
    plt.draw()
    #plt.show()
    plt.pause(0.05)    
    
    #print (soma_erros)
    #if soma_erros == 0: break

#pesos = weights
predicao = []
for i in range(nDados):
    entrada = dados[i]
    saida = fx[i]
    entrada_pesos = list(zip(entrada, pesos))
    saida_calculada = sum([e*p for e,p in entrada_pesos])
    predicao.append(saida_calculada)

    
plt.cla()
plt.clf()
plt.scatter(vet, fx)
plt.plot(vet, predicao, '-')
plt.ylabel('y=f(x)')
plt.xlabel('x')
plt.draw()
#plt.show()
plt.pause(0.05)    


