from sys import argv
from itertools import islice

def load(arq='entrada.txt'):
    n, m, obj = [],[],[] #inicializa n, m e a lista de objetos como objetos mutáveis
    with open(arq,'r') as entrada:
        n, m = (entrada.readline()).rstrip().split(" ") #extrai o n e m da primeira linha 
        obt = (list((islice(entrada,0,None)))) #salva o resto do arquivo em uma lista temporária
        for x in obt:
            unidade = list(map(int, x.rstrip().split(" "))) #converte em inteiros, salva na lista obj
            obj.append(unidade)
    m, n = int(m), int(n)
    
    return n,m,obj

def gulosa(n,m,obj):
    
    item_id = 1 # gerar um id para cada item p/ o resultado final

    for x in obj: #calcula o peso de cada item
        peso = x[1] / x[0] #valor / tamanho
        x.append(peso) #adiciona o peso na lista
        x.append(item_id)
        item_id += 1
    obj = sorted(obj, key=lambda x: x[2], reverse=True) #organiza do maior peso para o menor

    usado,valor,bagagem = 0,0,[] #inicializa as variaveis que iremos calcular

    while (usado < m) and obj: #enquanto a mochila não está cheia
        if (obj[0][0] + usado <= m) and obj: #se o objeto é menor do que o tamanho total da mochila
            bagagem.append(obj[0]) #inclui na bagagem
            usado += obj[0][0] #incrementa usado
            valor += obj[0][1] #incrementa o valor
            obj.pop(0) #remove da lista de objetos
        elif (obj[0][0] + usado > m) and obj: #se não cabe, remove da lista de objetos
            obj.pop(0)

    print("Solução Gulosa: \n Um Total de " + str(len(bagagem)) + " Itens: ", end='')
    for x in range(0, len(bagagem)): print(bagagem[x][3], end=', ')
    print("com o Valor Total de " + str(valor)) #imprime o resultaod final

def dinamica(n,m,obj):

    tabela = [[0 for q in range(m+1)] for t in range(n+1)] #cria uma tabela com linhas para cada item, e colunas para cada peso.
    for i in range(1,n+1): #loop de colunas
        for j in range(1,m+1): #loop das linhas
            if obj[i-1][0] <= j: 
                tabela[i][j] = max(tabela[i-1][j], obj[i-1][1] + tabela[i-1][j - obj[i-1][0]]) #procura o valor máximo
            else: tabela[i][j] = tabela[i-1][j] #caso contrário, retorna o valor da linha na coluna anterior

    # rotina para impressao de quais itens foram selecionados
    t_n, t_m, t_it = n, m, []

    while t_n and t_m > 0:
        if tabela[t_n][t_m] != tabela[t_n-1][t_m]: #se o valor da linha na coluna for diferente da coluna acima imediatamente desta, marca o valor 
            t_it.append(t_n)
            t_n -= 1
            t_m -= obj[t_n][0]
        else:
                t_n -= 1

    print("Solução Dinâmica: \n Um Total de " + str(len(t_it)) + " Itens: " ,end='')
    for x in t_it: print(x, end=', ')
    print("com o Valor Total de " + str(tabela[n][m]))


n,m,obj = load("mochila01.txt")

gulosa(n,m,obj)
dinamica(n,m,obj)