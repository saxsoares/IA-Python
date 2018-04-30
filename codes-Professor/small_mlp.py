# -*- coding: utf-8 -*-
"""
Prof. Dr. Vinicius Veloso de Melo
UC: IA 1/2018
ICT-UNIFESP
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoide (x, deriv=False):
    val = 1.0/(1.0 + np.exp(-x))
    if deriv: val = val*(1.0-val)
    return val

# Entrada
X = np.array ( [[0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# Saida
y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

# Pesos de duas camadas: -1 a 1
# Entrada: 3
# Camada 1: 4 neuronios
# Saida: 1 neuronio


# Altere este parametro e veja o comportament do erro ao longo das epocas
alfa = 0.01

pesos_camadas = [ 2*np.random.random((4, 3)) - 1,
            2*np.random.random((1, 4)) - 1 ]

n_camadas = len(pesos_camadas)

estimado = [0] * (n_camadas+1)
estimado[0] = X
vet_mae = []  # erro absoluto medio

for epoca in range(60000):
    for j in range(n_camadas):
        estimado[j+1] = sigmoide (np.dot(estimado[j], pesos_camadas[j].T))
                          
    erro = y - estimado[n_camadas]
    
    if (epoca % 1000) == 0:
        print "Epoca:" + str(epoca) + "  Erro:" + str(np.mean(np.abs(erro)))
        vet_mae.append(np.mean(np.abs(erro)))
            
    for j in range(n_camadas, 0, -1):
        delta_saida = erro * sigmoide(estimado[j], deriv=True)
        erro = delta_saida.dot(pesos_camadas[j-1])
        pesos_camadas[j-1] += alfa * estimado[j-1].T.dot(delta_saida).T

print "\nSaida estimada:"
print estimado[n_camadas]

plt.plot(vet_mae, 'k-')
plt.grid(1)
plt.draw()