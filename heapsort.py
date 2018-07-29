# APA - Atividade 3 - HeapSort/MaxHeap
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: heapsort.py [Arquivo de Entrada] [Arquivo de Saida]

import sys # para fazer parsing dos argumentos

def heap_max(heap, final, pos): #montando o max heap
    
    maior,esq,dir = pos, 2*pos + 1, 2*pos + 2
    
    if esq < final and heap[maior] < heap[esq]: maior = esq 
    if dir < final and heap[maior] < heap[dir]: maior = dir
        
    if maior != pos:
        heap[pos],heap[maior] = heap[maior],heap[pos] 
        heap_max(heap, final, maior)
        
def heap_sort(heap):
    n = len(heap)
    
    for x in range(int(n/2),-1,-1):
        heap_max(heap,n,x)
    
    for x in range(n-1,-1,-1):
        heap[0],heap[x] = heap[x], heap[0]
        heap_max(heap,x, 0)
    

#leitura dos arquivos
if len(sys.argv)< 2: print("ERRO - faltam argumentos. // Uso heapsort.py [ENTRADA] [SAIDA]"); exit()
else: entrada = sys.argv[1]; saida = sys.argv[2]
lista = open(entrada, 'r').readlines() # abre o arquivo e salva cada linha como o elemento de uma lista (python é mágico!)
for x in range(0, len(lista)): lista[x] = int(lista[x]) # loop para transformar a lista de strings em um array de inteiros. 

heap_sort(lista)
#print(lista)

with open(saida, 'w') as saida: #salvando em arquivo 
    for x in lista:
        saida.write("%i\n" %x) #escreve cada numero ordenado separado por linha

