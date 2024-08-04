from cicloEuleriano import Hierholzer
from Graph import OrientedGraph


if __name__ == "__main__":
    g = OrientedGraph(9)

    g.add_vertex_data(0, 'v1')
    g.add_vertex_data(1, 'v2')
    g.add_vertex_data(2, 'v3')
    g.add_vertex_data(3, 'v4')
    g.add_vertex_data(4, 'v5')
    g.add_vertex_data(5, 'v6')
    g.add_vertex_data(6, 'v7')
    g.add_vertex_data(7, 'v8')
    g.add_vertex_data(8, 'v9')

    g.add_edge(0, 1, 11)
    g.add_edge(0, 2, 9)
    g.add_edge(1, 3, 4)
    g.add_edge(1, 4, 8)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 6)
    g.add_edge(3, 5, 6)
    g.add_edge(3, 6, 5)
    g.add_edge(4, 6, 6)
    g.add_edge(4, 7, 4)
    g.add_edge(5, 8, 6)
    g.add_edge(6, 8, 4)
    g.add_edge(7, 8, 6)
    for vector in g.adj_matrix:
        print(vector)

    print("Algoritmo de Dijkstra, do vértice v1 ao vértice v9:")
    distance, path = g.dijkstra('v1','v9')
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
    cicloEuleriano1 = Hierholzer(grafo, 3)
    
    print("Ciclo Euleriano:", cicloEuleriano.hierholzer())
    print("Ciclo Euleriano iniciando pelo vertice 3:", cicloEuleriano1.hierholzer())
    
    