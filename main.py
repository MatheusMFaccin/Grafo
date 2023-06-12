from pyvis import Network
import networkx as nx

class Vertice:
    def __init__(self,index):
        self.index = index

class Aresta:
    def __init__(self,inicial,fim,custo,carga):
        self.inicial = inicial
        self.fim = fim
        self.custo = custo
        self.carga = carga
class Grafo:
    def __init__(self, arestas):
        self.arestas = arestas


f = open("arquivo.txt", "r")
Arquivo = f.read()
linhas = Arquivo.split("\n")
Vertices = []
Arestas = []
for linha in range(len(linhas)):
    if linha == 0:
        vertices = linhas[0].split(',')
        for vertice in vertices:
            Vertices.append(Vertice(vertice))
    else:
        arestas = linhas[linha].split(';')
        print(arestas)
        for aresta in arestas:
            if aresta:
                valores = aresta.split(',')
                if valores:
                    verticeInicial = valores[0]
                    verticeFinal = valores[1]
                    custo = valores[2]
                    carga = valores[3]
                    if any(vertice.index == verticeFinal for vertice in Vertices) and any(vertice.index==verticeInicial for vertice in Vertices): 
                        Arestas.append(Aresta(verticeInicial,verticeFinal,custo,carga))
net = Network()

for aresta in Arestas:
    print(aresta.inicial,aresta.fim,aresta.custo,aresta.carga)
    net.add_edge(aresta.inicial,aresta.fim, custo = aresta.custo, carga = aresta.carga)

custos = nx.get_edge_attributes(net, 'custo')
cargas = nx.get_edge_attributes(net, 'carga')
    
    



        
