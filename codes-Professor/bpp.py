import sys

# bpp = busca primeiro em profundidade
def bpp(grafo, inicio, fim, caminho=[]):
    caminho = caminho + [inicio]
    if inicio == fim:
        #print ("Cheguei!")
        return caminho
    if inicio not in grafo:
        return []
    for no in grafo[inicio]:
        #print (caminho, " -> ", no)
        if no not in caminho:
        novo_caminho = bpp(grafo, no, fim, caminho)
        if len(novo_caminho)>0:
            return novo_caminho
            #print ("Falhou!")
        #else:
            #print ("Ciclo!")
            return []

########################
# Main
########################
grafo = {}

# Le a primeira linha com inicio e fim
dados = sys.stdin.readline().strip().split(' ')

#print (dados)

inicio, fim = dados[0], dados[1]

# Le  o restante do arquivo
for dados in sys.stdin:
    dados = dados.strip().splip(' ')
    if dados:
        grafos[dados[0]] = dados[1:]
    else:
        break

#print (grafo)

print(bpp(grafo, inicio, fim, caminho=[]))
