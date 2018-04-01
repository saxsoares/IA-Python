import sys

def bpl(grafo, inicio, fim):
    fila = []
    fila.append([inicio])
    while(fila):
        caminho = fila.pop(0)
        no = caminho[-1]
        if no == fim: return caminho
        for adj in grafo.get(no, []):
            if adj not in caminho:
                novo_caminho = list(caminho)
                novo_caminho.append(adj)
                fila.append(novo_caminho)
                if adj == fim: return novo_caminho
    return []

grafo = {}
dados = sys.stdin.readline().strip().split(' ')
inicio, fim = dados[0], dados[1]
for dados in sys.stdin:
    dados = dados.strip().split(' ')
    if dados:
        grafo[dados[0]] = dados[1:]

print bpl(grafo, inicio, fim)
