
class Graph:
    
    def __init__(self,arquivo):
        self.graph = []
        n, adj = self.load(arquivo)
        self.vertices = self.build_vertices(n)
        self.n = n
        self.build_edgelist(n,adj)

    def load(self, arquivo='entrada.txt'): 
        adj = []

        with open(arquivo,'r') as entrada: #lê o arquivo especificado, linha por linha
            for line in entrada: 
                linha = list(map(int, line.rstrip().split(" ")))
                adj.append(linha)

        n = adj.pop(0); n = n[0]
        return n, adj

    def add_edge(self, pos_x,pos_y, valor):
        edge = pos_x, pos_y, valor
        edge2 = pos_y,pos_x, valor # desnecessário no kruskal
        self.graph.append(edge)
        self.graph.append(edge2)
    def build_vertices(self, n):
        vertices = []
        for x in range(n):
            vert = Vertice(x)
            vertices.append(vert)
        return vertices

    def build_edgelist(self, n, adj):
        p_x, p_y = 0, 1
        while adj:
            while adj[0]:
                self.add_edge(p_x,p_y, adj[0][0])
                adj[0].pop(0)
                p_y += 1
            adj.pop(0)
            p_x += 1
            p_y = p_x + 1

class Vertice:
    def __init__(self,idv):
        self.idv = idv
        self.visited = False
        self.distance = 999999999999999


def find(vertice, p):
    if p[vertice] != vertice: p[vertice] = find(p[vertice],p)
    return p[vertice]

def union(v1, v2,p,rank):
    raiz1,raiz2 = find(v1,p),find(v2,p)
    
    if raiz1 != raiz2:
        if rank[raiz1] > rank[raiz2]: p[raiz2] = raiz1
    else:
	    p[raiz1] = raiz2
    if rank[raiz1] == rank[raiz2]: rank[raiz2] += 1

def kruskal(graph):

    min_tree,p,rank = [],{},{}

    # montando os sets (make-set)
    for x in range(graph.n):
        p[x] = x
        rank[x] = 0

    edges = sorted(graph.graph, key=lambda x: x[2])
    edges.sort() #ordena do menor pro maior
    
    #monta a arvore minima
    for edge in edges:
        v1, v2, peso = edge
        if find(v1,p) != find(v2,p):
            union(v1, v2, p, rank)
            min_tree.append(edge)
            
    return sorted(min_tree, key=lambda x: x[2])
   


print(kruskal(Graph("entrada.txt")))
