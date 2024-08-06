import random
from cicloEuleriano import Hierholzer
from Graph import OrientedGraph

import time

if __name__ == "__main__":
    
    g = OrientedGraph(6)

    g.add_vertex_data(0, 'v1')
    g.add_vertex_data(1, 'v2')
    g.add_vertex_data(2, 'v3')
    g.add_vertex_data(3, 'v4')
    g.add_vertex_data(4, 'v5')
    g.add_vertex_data(5, 'v6')

    g.add_edge(0, 1, 3)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 3, 7)
    g.add_edge(1, 4, 1)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 5)
    
    distance, path = g.dijkstra('v1','v6')
    print(f"Caminho: {path}, Distância: {distance}")
    


    grafo = {
        1: [2, 3],
        2: [1, 3, 4, 5],
        3: [1, 2, 4, 5],
        4: [2, 3, 5, 6],
        5: [2, 3, 4, 6],
        6: [4, 5]
    }

    cicloEuleriano = Hierholzer(grafo)
    print("Ciclo Euleriano:", cicloEuleriano.hierholzer())

    
    