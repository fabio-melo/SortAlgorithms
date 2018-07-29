# APA - Atividade 2 - QuickSort
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: quicksort.py [Arquivo de Entrada] [Arquivo de Saida]

import sys,random # para fazer parsing dos argumentos

# funcao recursiva do quicksort
def quicksort(lista,min,max):
    if min < max:
        p =  part(lista,min,max)
        quicksort(lista,min,p-1)
        quicksort(lista,p+1,max)
    return lista

# funcao de particionamento
def part(p, min, max):
    
    pivot_pos = random.randint(min,max) # escolhe uma posicao aleatoria entre minimo e maximo como pivot
    pivot = p[pivot_pos] #armazena o valor, para comparacoes
    p[pivot_pos],p[max] = p[max],p[pivot_pos] # troca o valor da posição maxima com a do pivot
    
    i = min - 1 #inicializando o i
    
    for j in range(min,max):
        if p[j] <= pivot:
            i = i+1 # incrementa, iniciando de para que a primeira posicao possivel seja 0
            p[i],p[j] = p[j],p[i] 
            
    p[i+1], p[max] = p[max],p[i+1]
    return i+1 #retorna a posicao final do pivot

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

#chamada do algoritimo
lista = quicksort(lista, 0, len(lista)-1)

#print(lista) # printa a lista ordenada

with open(saida, 'w') as saida: #salvando em arquivo 
    for x in lista:
       saida.write("%i\n" %x) #escreve cada numero ordenado separado por linha

