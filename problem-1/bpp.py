import sys

def bpp(grafo, inicio, fim, caminho=[]):
    
    caminho = caminho + [inicio]
    if (inicio == fim):
        print("Cheguei!\n")
        return caminho
    if inicio not in grafo:
        return[]
    for no in grafo[inicio]:
        print(caminho, " -> ", no)
        if no not in caminho:
            novo_caminho = bpp(grafo, no, fim, caminho)
            if len(novo_caminho)>0: return novo_caminho
            print ("Falhou!")
        else:
            print ("Ciclo!")
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

for k, v in sorted(grafo.items()):
    print(str(k)  + ": " + str(v))

print 
print(bpp(grafo, inicio, fim, caminho=[]))

