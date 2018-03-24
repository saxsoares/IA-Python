import sys

def bpp(grafo, inicio, fim, caminho=[]):
    return []

grafo = {}

dados = sys.stdin.readline().strip().split(' ')

inicio, fim = dados[0], dados[1]

for dados in sys.stdin:
    dados = dados.strip().split(' ')
    if dados:
        grafo[dados[0]] = dados[1:]
    else:
        break

print(grafo)

print(bpp(grafo, inicio, fim, caminho=[]))

