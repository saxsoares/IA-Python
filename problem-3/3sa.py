import sys
import random
import math

def objfun(x):
  # print (x)
  return 10 * math.sin(0.3 * x) * math.sin (1.3 * x**2) + 0.00001 * x**4 + 0.2*x + 80

###############################################################
#
# IMPLEMENTE AQUI A FUNCAO Vizinho (S, li, ls, passo)
def Vizinho( S, li, ls, passo):
    Si = S + random.uniform(-passo, passo)
    if(Si < li): Si = li
    elif( Si > ls): Si = ls
    return Si
#
###############################################################

def sa (fun, S0, li, ls, maxIter, alfa, T0):
    S = S0
    melhorSol = S
    melhorVal = fun(S)
    melhorIter = 0
    passo = (ls-li)/10.0
    T = T0
    j = 0

    random.seed(1)
       
    while (j < maxIter):
        Si = Vizinho (S, li, ls, passo)
        delta = fun(Si) - fun(S)
        if delta <= 0 or random.uniform(0, 1) < math.exp(-delta/T):
            S = Si
            # print "Nova sol=", S, "valor=", fun(S)
            if fun(S) < melhorVal:
                melhorVal = fun(S)
                melhorSol = S
                melhorIter = j
                # print ">>> Nova melhorSol=", S, "melhorVal=", melhorVal

        T = T * alfa
        j = j + 1
        # print "Temp=", T
        
    return [melhorSol, melhorVal]
    

########################
# Main
########################
         
# Le a linha com as configuracoes
config = sys.stdin.readline().strip().split(' ')

# Converte os textos para float
config = [float(val) for val in config]

# Chama a funcao sa com os parametros lidos
result = sa(objfun, *config)
print "%.5f %.5f" % (result[0], result[1])
   
