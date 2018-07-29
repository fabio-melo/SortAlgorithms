from itertools import islice,combinations

def load(arq='pcv04.txt'):
    n, mat = [],[] #inicializa n, m e a lista de objetos como objetos mutáveis
    with open(arq,'r') as entrada:
        n = int((entrada.readline()).rstrip()) #extrai o n da primeira linha 
        tmp = (list((islice(entrada,0,None)))) #salva o resto do arquivo em uma lista temporária
        for x in tmp:
            unidade = list(map(int, x.rstrip().split(" "))) #converte em inteiros, salva na lista
            mat.append(unidade)
    
    return n, mat

def held_karp(mat,n):

    mat_d = {(frozenset([0, x+1]), x+1): (dist, [0,x+1]) for x,dist in enumerate(mat[0][1:])}
    # Utilizando a matriz de entrada como iterador, para montar o dicionário inicial 
    # Dicionário/Matriz de Distancias gerado:
    # Chave: set imutável (frozenset) com itens percorridos, rota escolhida
    # Valor: distancia percorrida, caminho feito
    
    for m in range(2, n): #executa para cada linha da matriz
        tmp = {} #dicionario temporario, que será atualizado com os novos valores
        for S in [frozenset(C) | {0} for C in combinations(range(1, n), m)]: # para cada possivel combinação de 
            for j in S - {0}: # loop que adiciona no dicionario os novos subsets (partes) do caminho percorridas e seus valores minimos
                tmp[(S, j)] = min( [(mat_d[(S-{j},k)][0] + mat[k][j], mat_d[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])
        mat_d = tmp # atualiza o dicionário com os novos valores

    # o Resultado é a entrada no dicionário cujo caminho possui o valor mínimo.
    res = min([(mat_d[d][0] + mat[0][d[1]], mat_d[d][1]) for d in iter(mat_d)]) 

    res[1].append(0) #adiciona o início no código
    print("Custo Total: " + str(res[0]) + ", Caminho: " + str(res[1]))


n, mat = load("pcv04.txt")

held_karp(mat, n)