import sys

def bpl(grafo, inicio, fim):
    # Armazena a fila de caminhos
    fila = []
    # insere o primeiro caminho no fim da fila
    fila.append([inicio])
    while fila:
        #print ("Fronteira=", fila)
        # Pega, da primeira posicaoo, o proximo caminho da fila
        caminho = fila.pop(0)
        # pega o ultimo no do caminho, para saber com quem ele deve ser conectado
        no = caminho[-1]
        # caminho found
        if no == fim: return caminho
        # Constroi novos caminhos ligando a cada um dos nos adjacentes
        for adjacente in grafo.get(no, []): # Caso nao haja o no, return []
            if adjacente not in caminho: # Caso ainda nao tenha sido visitado
                #print (caminho, "->", adjacente)
                novo_caminho = list(caminho)
                novo_caminho.append(adjacente)
                fila.append(novo_caminho)
                if adjacente == fim:
                #   #print ("Cheguei!")
                    return(novo_caminho)
    return []

# Main

grafo = {}

dados = sys.stdin.readline().strip().split(' ')
inicio, fim = dados[0], dados[1]

for dados in sys.stdin:
    dados = dados.strip().split(' ')
    if dados:
        grafo[dados[0]] = dados[1:]

print (bpl(grafo, inicio, fim))

