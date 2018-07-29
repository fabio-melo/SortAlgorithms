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

# Monta uma matriz de tamanho n por n, populada por zeros.
def build_matrix(n):
    matrix = []
    for x in range(n):
        matrix.append([])
        for y in range(n):
            matrix[x].append(0)
    return matrix

# popula a matrix com os pesos dos caminhos 
def fill_matrix(matrix,graph):
    for x in range(len(graph)):
        matrix[graph[x][0]][graph[x][1]] = graph[x][2]
        matrix[graph[x][1]][graph[x][0]] = graph[x][2]
    return matrix

# algoritmo PRIM para gerar arvore minima
def prim(matrix, n):
  
    pos = 0 #começando da posição zero
    min_tree,visited,edges = [],[],[] #inicializando listas de visitados e arestas
    min_edge = [None,None,float('inf')] #iniciamente, o valor da aresta é infinito e nunca foi visitado

    while len(min_tree) != n-1: #enquanto a min-tree nao estiver completamente formada

        visited.append(pos) #marca posicao visitada
        #faz iteração na matriz e adiciona na lista de arestas
        for x in range(n):
            if matrix[pos][x] != 0: #se a posição não for nula
                edges.append([pos,x,matrix[pos][x]]) #adiciona na lista de arestas

        #busca pela aresta com menor valor
        for x in range(len(edges)): 
            if edges[x][2] < min_edge[2] and edges[x][1] not in visited:
                min_edge = edges[x]
        # remove da lista de arestas
        edges.remove(min_edge)
        min_tree.append(min_edge)
        # nova posição é o parente da aresta minima
        pos = min_edge[1]
        min_edge = [None,None,float('inf')] #reseta o min_edge
    
    return min_tree #após o loop retorna a arvore gerada
  

graf = []
n, adj = load('entrada.txt')
build_adjlist(n,adj,graf)
matriz = fill_matrix(build_matrix(n),graf)
print (prim(matriz,n))
