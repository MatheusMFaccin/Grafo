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
                print(valores)
                Arestas.append(Aresta(valores[0],valores[1],valores[2],valores[3]))

for aresta in Arestas:
    print(aresta.inicial,aresta.fim,aresta.custo,aresta.carga)
        