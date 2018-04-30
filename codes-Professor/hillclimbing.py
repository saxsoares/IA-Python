# hill-climbing

import matplotlib.pyplot as plt
import random

random.seed(10)

def objfun (x):
  return va * x**2 + vb*x + vc


va = 1
vb = -5
vc = 30

xmin = -100
xmax = 100
# dim = 1

qtd_pontos = 100

passo = (xmax-xmin)/(qtd_pontos-1)
vet = [xmin]
for i in range(1, qtd_pontos):
    vet.append (vet[-1]+passo)
    
fx = []
for i in range(len(vet)):
  fx.append(objfun(vet[i]))

fx2 = []
for v in vet:
  fx2.append(objfun(v))

fx3 = [objfun(valor) for valor in vet]

#### plot da superficie de resposta
#set.seed(1)


minx=-vb/2*va
delta = (-vb)**2 - 4*va*vc
miny = -delta/4*va

plt.cla()
plt.clf()
plt.plot (vet, fx, "b")
plt.plot (minx, miny, "g", marker = "x", markersize = 12, linewidth = 10, markeredgewidth = 2)
plt.ylabel('y=f(x)')
plt.xlabel('x')
plt.draw()
plt.show()


max_iteracoes = 3000

historico = []

sol = random.uniform(xmin, xmin+2)
y = objfun (sol)
  
melhor_sol = sol
melhor_y = y

for iter in range(max_iteracoes):
  
  perturbacao = random.uniform(xmin, xmax)

  sol_teste = sol + perturbacao
  y_teste = objfun (sol_teste)

  if y_teste <= y:
      sol = sol_teste
      y = y_teste
  
      if y <= melhor_y:
          melhor_sol = sol
          melhor_y = y

  plt.plot (sol, y, "go", markersize = 7)
  plt.text (sol, y, str(iter))
  plt.draw()
  plt.pause(0.5)    
    
  historico.append([sol, y])
  
          
plt.plot (melhor_sol, melhor_y, "rx", markersize = 10, markeredgewidth = 5)

plt.draw()
plt.show()
  

