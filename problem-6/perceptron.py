# coding=utf-8
import random
import sys

def perceptron (semente, alfa, max_epocas, entradas, saidas):

    degrau = lambda u: 1 if u >= 0 else 0
    ativacao = degrau

    random.seed(semente)

    # Adicionar o elemento neutro para o bias
    #entradas = [ [1] + e for e in entradas ]
    entradas = map(lambda e: [1] + e, entradas )    # Exemplo usando a funcao map para aplicar a funcao anonima lambda a cada entrada

    nDados = len(entradas)
    nDim = len(entradas[0])

    # Inicializar pesos arbitrariamente
    pesos = [random.random() for _ in range(nDim)]

    for epoca in range(max_epocas):
        soma_erros = 0

        for j in range(nDados):
            
            saida_calculada = ativacao(sum([e*p for e,p in list(zip(entradas[j],pesos))]))
            erro = saidas[j] - saida_calculada
            soma_erros += abs(erro)

            pesos = [p + alfa * erro * e for e,p in list(zip(entradas[j],pesos))]

    # IMPRIME AS INFORMACOES DESEJADAS
    #print("Lista de Entrada;Saida;Potencial;Saida Calculada")
    for j in range(nDados):
        potencial = sum([pesos[i]*entradas[j][i] for i in range(nDim)])
        saida_calculada = ativacao(potencial)
        erro = saidas[j] - saida_calculada
        print("{};{};{:.3f};{}".format(entradas[j], saidas[j], potencial, saida_calculada))



##########################################
#
#  MAIN
#
##########################################

# Le a primeira linha a semente, o alfa e a quantidade de epocas
semente, alfa, max_epocas, n = sys.stdin.readline().strip().split(';')

semente = int(semente)
alfa = float(alfa)
max_epocas = int(max_epocas)
n = int(n)

# Le o restante do arquivo convertendo os dados para inteiro. Primeiro, todas as n entradas. Depois, as n saidas.
entradas = [map(int, sys.stdin.readline().strip().split(';')) for _ in range(n)]
saidas = [int(sys.stdin.readline()) for _ in range(n)]

perceptron(semente, alfa, max_epocas, entradas, saidas)
