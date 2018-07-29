import collections, heapq

#carregamento de arquivo
def load(arquivo='entrada.txt'): 
    adj = []
    with open(arquivo,'r') as entrada: #lê o arquivo especificado e extrai os valores
        for line in entrada: 
            linha = list(map(int, line.rstrip().split(" ")))
            adj.append(linha)
    n = adj.pop(0); n = n[0] #extrai o 'n'
    return n, adj
#salva uma aresta do vertice na lista do grafo
def add_edge(pos_x,pos_y, valor,g):
        edge = [pos_x, pos_y, valor]
        edge2 = [pos_y,pos_x, valor]
        g.append(edge)
        g.append(edge2)

#monta a lista de adjacencia em uma lista
def build_adjlist(n, adj,g):
    p_x, p_y = 0, 1
    while adj:
        while adj[0]:
            add_edge(p_x,p_y, adj[0][0],g)
            adj[0].pop(0)
            p_y += 1
        adj.pop(0)
        p_x += 1
        p_y = p_x + 1



#algoritmo de djsktra

def dijkstra(edges, g, f, n):
    for x,y,z in edges:
        g[x].append((z,y))

    q = [(0,f,())]
    seen = []
    while q:
        (cost,v1,path) = heapq.heappop(q)
        if v1 not in seen:
            seen.append(v1)
            path = (v1, path)
            if v1 == n: return cost, path #achou o menor caminho, retorna

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heapq.heappush(q, (cost+c, v2, path)) #relaxamento de função

    return float("inf") #caminho infinito


    
edges, edge_d = [], collections.defaultdict(list)
n, adj = load('entrada.txt')
build_adjlist(n,adj,edges)

cost, path =  dijkstra(edges, edge_d, 0, n-1)

path = list(filter(None, str(path).rstrip().replace('(','').replace(')','').replace(' ','').split(',')))
print("Custo Total do Caminho: " + str(cost))
print("Caminho: " + str(path) )