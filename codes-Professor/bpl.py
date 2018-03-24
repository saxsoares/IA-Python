﻿import sys

# bpl = busca primeiro em largura        
def bpl(grafo, inicio, fim):
    # Armazena a fila de caminhos
    fila = []
    # Insere o primeiro caminho no fim da fila
    fila.append([inicio])
    while fila:
        #print ("Fronteira=", fila)
        #print (fila)
        # Pega, da primeira posição, o próximo caminho da fila
        caminho = fila.pop(0)
        # Pega o último nó do caminho, para saber com quem ele deve ser conectado
        no = caminho[-1]
        # caminho found
        if no == fim:
            #print ("Cheguei!")
            return caminho
        # Constrói novos caminhos ligando a cada um dos nós adjacentes
        for adjacente in grafo.get(no, []):   # Caso não haja o nó, retorne []
            if adjacente not in caminho:  # Caso ainda não tenha sido visitado
               #print (caminho, "->", adjacente)
               novo_caminho = list(caminho)
               novo_caminho.append(adjacente)
               fila.append(novo_caminho)
               if adjacente == fim:
                   #print ("Cheguei!")
                   return (novo_caminho)
    #print ("Caminho inexistente!")
    return []
        

########################
# Main
########################
    
###############################
# IMPLEMENTE O CODIGO AQUI
###############################
