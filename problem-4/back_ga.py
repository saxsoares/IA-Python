import random
import sys

def avalia_senha(ind, senha):
    return [c1 == c2 for c1, c2 in zip(ind, senha)].count(True)

def cria_ind (nDim, opcoes):
    # random.sample retorna uma lista. Logo, pegue o 1o. elemento.
    return [ random.sample(opcoes, 1)[0] for i in range(nDim)]  


def cria_pop (nDim, tamPop, opcoes):
    return [cria_ind (nDim, opcoes) for qtd in range(tamPop)]

def mutacao (ind, probMut, opcoes):
    for i in range(len(ind)):
        if (random.uniform(0, 1) < probMut):
            ind[i] = random.sample(opcoes, 1)[0]
    return ind

def cruzamento (ind1, ind2):
    corte = random.sample(range(1, len(ind1)), 1)[0]
    return ind1[:corte] + ind2[corte:]

def torneio (aptidao, tamanho):
    id_compet = range(len(aptidao))
    competidores = random.sample(id_compet, tamanho)
    fit = [aptidao[idx] for idx in competidores]
    v1 = competidores[fit.index(min(fit))]
    
    id_compet.remove(v1)
    competidores = random.sample(id_compet, tamanho)
    fit = [aptidao[idx] for idx in competidores]
    v2 = competidores[fit.index(min(fit))]
    
    return v1, v2
    

def ga(fun, senha, nDim, opcoes, tamPop, tamTorneio, probMut, porcCr, nGeracoes):
    pop = cria_pop (nDim, tamPop, opcoes)
    aptidao = [fun(indiv, senha) for indiv in pop]

    for ger in range(nGeracoes):        
        for cruzamentos in range( int(tamPop*porcCr) ):
            vencedor1, vencedor2 = torneio(aptidao, tamTorneio)

            pai1 = pop[vencedor1]
            pai2 = pop[vencedor2]
            filho = cruzamento (pai1, pai2)
            filho = mutacao (filho, probMut, opcoes)

            # Inserir na pop para depois selecionar apenas os melhores
            pop.append(filho)
            aptidao.append(fun(filho, senha))

        # Somente os melhores sobrevivem. Pra isso, descubra a ordem decrescente  
        # da aptidao, da melhor para a pior
        # Ordenar a lista [0, ..., tamPop-1] usando os valores de aptidao como referencia
        ordem = sorted(range(len(aptidao)), key=lambda k: aptidao[k], reverse=True)

        # Selecionar os tamPop melhores
        for idx in range(tamPop):
            aptidao[idx] = aptidao[ ordem[idx] ]
            pop[idx] = pop[ ordem[idx] ]
        
        # Eliminar o restante
        aptidao = aptidao[:tamPop]
        pop = pop[:tamPop]
        
        if False:
            print ("Ger:", ger, "  fit=", aptidao[0], " Melhor sol=", ''.join(pop[0]), 
            "  pior sol=", ''.join(pop[tamPop-1]))

        # Criterio de parada: a quantidade de acertos == tamanho da senha
        if (aptidao[0] == nDim):
            break
        
    return ''.join(pop[0])


########################
# Main
########################
         
# Le a linha com as configuracoes
config = sys.stdin.readline().strip().split(';')

random.seed(int(config[0]))

opcoes = "abcdefghijklmnopqrstuvwxyz "

# Chama a funcao sa com os parametros lidos
result = ga(fun=avalia_senha, 
            senha=config[1],
            nDim=len(config[1]), 
            opcoes=opcoes,
            tamPop=int(config[2]), 
            tamTorneio=int(config[3]),
            probMut=float(config[4]),
            porcCr=float(config[5]),
            nGeracoes=int(config[6]))

print (result)

   
