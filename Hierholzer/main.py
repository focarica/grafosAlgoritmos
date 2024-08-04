from cicloEuleriano import Hierholzer

if __name__ == "__main__":
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
    
    
    grafo2 = {
        'A': ['B', 'D'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['A']
    }
    
    cicloEuleriano2 = Hierholzer(grafo2)
    print(cicloEuleriano2.hierholzer())
    
    