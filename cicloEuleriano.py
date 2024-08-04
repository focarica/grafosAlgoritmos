from copy import deepcopy

def hierholzer(grafo: dict):
    
    # Verifica se todos os vértices têm grau par
    for v in grafo:
        if len(grafo[v]) % 2 != 0:
            return 'Grafo Não Euleriano'


    ciclo = []
    subciclo = []
    
    # Grafo auxiliar para nao modificar o original
    arestas = deepcopy(grafo)

    # Escolha um vértice inicial arbitrário com arestas
    for v in grafo:
        if grafo[v]:
            vertice_inicial = v
            break

    while True:
        subciclo.append(vertice_inicial)
        
        # Enquanto tiver alguma aresta não percorrida ligando o vertice
        while arestas[vertice_inicial]:
            
            # Remove a primeira aresta da lista do vertice atual. De ambos os lados
            proximo_vertice = arestas[vertice_inicial].pop(0)
            arestas[proximo_vertice].remove(vertice_inicial)
            
            
            vertice_inicial = proximo_vertice
            subciclo.append(vertice_inicial)

        if not ciclo:
            ciclo = subciclo
        else:
            index = ciclo.index(subciclo[0])
            ciclo = ciclo[:index] + subciclo + ciclo[index + 1:]

        for i in range(len(ciclo)):
            if arestas[ciclo[i]]:
                vertice_inicial = ciclo[i]
                subciclo = []
                break
        else:
            break

    return ciclo

# Grafo de exemplo: todos os vértices têm grau par

grafo = {
    1: [2, 3],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [2, 3, 5, 6],
    5: [2, 3, 4, 6],
    6: [4, 5]
}




ciclo_euleriano = hierholzer(grafo)
print("Ciclo Euleriano:", ciclo_euleriano)
