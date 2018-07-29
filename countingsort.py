# APA - Atividade 4 - CountingSort
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: countingsort.py [Arquivo de Entrada] [Arquivo de Saida]
# Recebe um arquivo com NÚMEROS INTEIROS POSITIVOS como entrada.

import sys # para fazer parsing dos argumentos


def csort(lista):

    maiornum = max(lista) #pega o maior numero da lista e usa como tamanho para a lista de contagem
    
    count_arr = [0 for x in range(maiornum + 1)] #aloca a lista de contagem
    
    for x in range(0,len(lista)): #monta a lista da contagem de ocorrencias
        count_arr[lista[x]] = count_arr[lista[x]] + 1

    for x in range(1,len(count_arr)): #modifica a lista de forma que os numeros sejam suas posições na lista
        count_arr[x] = count_arr[x] + count_arr[x-1]
    
    sorted = [0 for x in range(len(lista))] #aloca a lista que irá ser ordenada
    
    for x in range(len(lista)-1,-1,-1): #começa a ordenação
        sorted[count_arr[lista[x]]-1] = lista[x] #salva o item na sua posição final
        count_arr[lista[x]] = count_arr[lista[x]] - 1 #decrementa o numero na posição manipulada da lista
        
    return sorted #retorna a lista ordenada




# lista = [9,9,9,4,4,2,2,2,2,3,4,4,257,5,5,5,8,9,11,15,20,84,128]

# leitura dos arquivos
if len(sys.argv)< 2: print("ERRO - faltam argumentos. // Uso countingsort.py [ENTRADA] [SAIDA]"); exit()
else: entrada = sys.argv[1]; saida = sys.argv[2]
lista = open(entrada, 'r').readlines() # abre o arquivo e salva cada linha como o elemento de uma lista (python é mágico!)
for x in range(0, len(lista)): lista[x] = int(lista[x]) # loop para transformar a lista de strings em um array de inteiros. 

lista = csort(lista) #executa o couting sort

# print(lista) #

with open(saida, 'w') as saida:
    for x in lista: saida.write("%i\n" %x) #escreve no arquivo cada numero ordenado separado por linha