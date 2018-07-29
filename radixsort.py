# APA - Atividade 4 - RadixSort
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: radixsort.py [Arquivo de Entrada] [Arquivo de Saida]
# Recebe um arquivo com NÚMEROS INTEIROS POSITIVOS como entrada.

import sys # para fazer parsing dos argumentos

def radixsort(lista):
    
    qtde_it = len(str(max(lista))) #descobre a quantidade de digitos do maior numero da lista
    
    sorted = [0 for x in range(len(lista))] # cria um array de mesmo tamanho da lista, inicializado com zeros

    digito = 1 # começando do digito menos significante
    
    while qtde_it > 0: #itera até a maior potencia da lista

        balde = [0 for x in range(10)] # cria os baldes para os caracteres de 0 a 9.
        
        # faz o counting sort no digito da potencia
        for x in range(len(lista)): 
            balde[int((lista[x] / digito) % 10)] = balde[int((lista[x] / digito)%10)] + 1
        
        for x in range(1,len(balde)):
            balde[x] = balde[x] + balde[x-1]

        for x in range(len(lista)-1, -1, -1):
            balde[int((lista[x] / digito) % 10)] = balde[int((lista[x] / digito) % 10)] - 1
            sorted[balde[int((lista[x] / digito) % 10)]] = lista[x]
        
        for x in range(0, len(lista)): lista[x] = sorted[x] # copia a lista semi-organizada para a lista que vamos retornar
        
        digito = digito * 10 #incrementa a potencia
        
        qtde_it = qtde_it - 1 #reduz a qtde iterações do while

    return lista #retorna a lista ordenada


#leitura dos arquivos
if len(sys.argv)< 2: print("ERRO - faltam argumentos. // Uso radixsort.py [ENTRADA] [SAIDA]"); exit()
else: entrada = sys.argv[1]; saida = sys.argv[2]
lista = open(entrada, 'r').readlines() # abre o arquivo e salva cada linha como o elemento de uma lista (python é mágico!)
for x in range(0, len(lista)): lista[x] = int(lista[x]) # loop para transformar a lista de strings em um array de inteiros. 

lista = radixsort(lista)

with open(saida, 'w') as saida:
    for x in lista: saida.write("%i\n" %x) #escreve no arquivo cada numero ordenado separado por linha