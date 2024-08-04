from copy import deepcopy


class Hierholzer:
    
    
        def __init__(self, grafo: dict, verticeInicial = None):
            '''
            grafo = dicionario de dados contendo a lista de adjacencia de todos os vertices do grafo\n
            verticeInicial = Primeiro adicionado; caso nenhum for passado
            '''
            
            
            self.grafo = grafo
            self.verticeInicial = verticeInicial
        
        
        def isImpar(self):
            for v in self.grafo:
                if len(self.grafo[v]) % 2 != 0:
                    return True

        # Se o vertice inicial n for passado sera o primeiro que for adicionado.
        def escolhaVerticeInicial(self):
            if self.verticeInicial == None:
                for v in self.grafo:
                    if self.grafo[v]:
                        self.verticeInicial = v
                        break

        def hierholzer(self):            
            if self.isImpar():
                return "Grafo Não Euleriano"
            
            self.escolhaVerticeInicial()
            
            ciclo = []
            subciclo = []
            
            # Grafo auxiliar para nao modificar o original
            arestas = deepcopy(self.grafo)

            while True:
                subciclo.append(self.verticeInicial)
                
                # Enquanto tiver alguma aresta não percorrida ligando o vertice
                while arestas[self.verticeInicial]:
                    
                    # Remove a primeira aresta da lista do vertice atual. De ambos os lados
                    proximo_vertice = arestas[self.verticeInicial].pop(0)
                    arestas[proximo_vertice].remove(self.verticeInicial)
                    
                    self.verticeInicial = proximo_vertice
                    subciclo.append(self.verticeInicial)

                # Verifica se ja existe algum ciclo existente; se cair no else um novo subciclo é inserido no ciclo principal
                if not ciclo:
                    ciclo = subciclo
                else:
                    index = ciclo.index(subciclo[0])
                    ciclo = ciclo[:index] + subciclo + ciclo[index + 1:]

                # Verifica se após a criação do ciclo ainda existe algum aresta não percorrida, se sim vai para ela e reinicia o algoritmo
                for i in range(len(ciclo)):
                    if arestas[ciclo[i]]:
                        self.verticeInicial = ciclo[i]
                        subciclo = []
                        break
                else:
                    break

            return ciclo
