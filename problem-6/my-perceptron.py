# coding=utf-8
import random
import sys

def perceptron (semente, alfa, max_epocas, entradas, saidas):

    # settar semente rand
    # definir funcao ativacao
    # adicionar o elemento neutro para o bias
    

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
