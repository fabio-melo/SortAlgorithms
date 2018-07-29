# APA - Atividade 2 - MergeSort
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: mergesort.py [Arquivo de Entrada] [Arquivo de Saida]

import sys # para fazer parsing dos argumentos

def mergesort(lista):
    if len(lista) <= 1: # se a lista só possuir um item, retornar a lista.
        return lista
    # alocando lista esquerda e direita
    l_esq = []
    l_dir = []
    
    for i in range(0, len(lista)):
        if i < len(lista)/2:
            l_esq.append(lista[i])
        else:
            l_dir.append(lista[i])
    
    l_esq = mergesort(l_esq)
    l_dir = mergesort(l_dir)
    
    return join(l_esq,l_dir)
    
def join(esq,dir):
    res = []
    
    while esq and dir:
        if esq[0] <= dir[0]:
            res.append(esq[0])
            esq.pop(0)
        else:
            res.append(dir[0])
            dir.pop(0)
    
    while esq:
        res.append(esq[0])
        esq.pop(0)
    while dir:
        res.append(dir[0])
        dir.pop(0)
    return res
    

# base comum para a leitura dos arquivos
if len(sys.argv)< 2:
    print("ERRO - faltam argumentos. // Uso insertionsort.py [ENTRADA] [SAIDA]")
    exit()
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]
    
lista = open(entrada, 'r').readlines() # abre o arquivo e salva cada linha como o elemento de uma lista (python é mágico!)

for x in range(0, len(lista)):  # loop para transformar a lista de strings em um array de inteiros. 
    lista[x] = int(lista[x])

#chamada do mergesort
    
lista = mergesort(lista)

#print(lista) # printa a lista ordenada

with open(saida, 'w') as saida: #salvando em arquivo 
    for x in lista:
        saida.write("%i\n" %x) #escreve cada numero ordenado separado por linha

