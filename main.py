from pyvis.network import Network
import networkx as nx

class Vertice:
    def __init__(self,index):
        self.index = index

class Aresta:
    index=0
    def __init__(self,inicial,fim,custo,carga,eficiencia):
        self.index = Aresta.index
        self.inicial = inicial
        self.fim = fim
        self.custo = custo
        self.carga = carga
        self.eficiencia = eficiencia
        Aresta.index+=1

class Grafo:
    def __init__(self, arestas):
        self.arestas = arestas


net = Network(notebook=True,directed=True,height='500px', width='100%')
nxgraph = nx.cycle_graph(10)
f = open("arquivo.txt", "r")
Arquivo = f.read()
linhas = Arquivo.split("\n")
Vertices = []
Arestas = []
eficiencias = []
mapa = []
index = 0 
for linha in range(len(linhas)):
    if linha == 0:
        linhaVertices = linhas[0].split(',')
        for vertice in linhaVertices:
            Vertices.append(Vertice(int(vertice)))
            
    else:
        linhaArestas = linhas[linha].split(';')
        print(linhaArestas)
        for aresta in linhaArestas:
            if aresta:
                valores = aresta.split(',')
                if valores:
                    verticeInicial = int(valores[0])
                    verticeFinal = int(valores[1])
                    custo = float(valores[2])
                    carga = float(valores[3])
                    eficiencia = carga/custo
                    #verifica se os vertices estao adicionados na lista de vertice se eles estiverem ele vai adicionar a aresta na lista arestas 
                    if any(vertice.index == verticeFinal for vertice in Vertices) and any(vertice.index==verticeInicial for vertice in Vertices): 
                        Arestas.append(Aresta(verticeInicial,verticeFinal,custo,carga,eficiencia))


for vertice in Vertices:
   
   
    net.add_node(int(vertice.index), label="vertice "+str(vertice.index),shape="circle",color="#fa8072")
arestasOrdenadas = sorted(Arestas, key=lambda  obj: -obj.eficiencia)
i = 0
for aresta in arestasOrdenadas:
    if i == 0:    
        print(aresta.inicial,aresta.fim,aresta.custo,aresta.carga)
        resultado = round(aresta.custo/aresta.carga,2)
        eficiencias.append(resultado)
        net.add_edge(int(aresta.inicial),int(aresta.fim),color="#0000ff",weight=5,title="custo da rota: "+str(aresta.custo)+" tamanho da carga: "+str(aresta.carga)+" eficiencia da rota: "+str(resultado))
    else:
        print(aresta.inicial,aresta.fim,aresta.custo,aresta.carga)
        resultado = round(aresta.custo/aresta.carga,2)
        eficiencias.append(resultado)
        net.add_edge(int(aresta.inicial),int(aresta.fim),weight=5,title="custo da rota: "+str(aresta.custo)+" tamanho da carga: "+str(aresta.carga)+" eficiencia da rota: "+str(resultado))
    i+=1


for aresta in arestasOrdenadas:
    print("aresta mais eficiente para a menos eficiente")    
    print(aresta.inicial,aresta.fim,aresta.custo,aresta.carga, aresta.eficiencia)



net.show('index.html')
    
    



        
