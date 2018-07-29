# APA - Atividade 1 - SelectionSort
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: selectionsort.py [Arquivo de Entrada] [Arquivo de Saida]

import sys # para fazer parsing dos argumentos

if len(sys.argv)< 2:
    print("ERRO - faltam argumentos. // Uso selectionsort.py [ENTRADA] [SAIDA]")
    exit()
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]
#   print(entrada)
#  print(saida)
    

lista = open(entrada, 'r').readlines() # abre o arquivo e salva cada linha como o elemento de uma lista (python é mágico!)

for x in range(0, len(lista)): # transforma a lista de string para int
    lista[x] = int(lista[x])
    
for i in range(0, len(lista)): #a ordenacao ocorre aqui
    for j in range(i+1, len(lista)): #iteracao pra frente
        if lista[i] > lista[j]: #substitui o valor de i pelo menor item, se encontrado
            lista[i], lista[j] = lista[j],lista[i]  #troca-troca
               
print(lista) #imprime pra ver se tá tudo certinho

with open(saida, 'w') as saida: #salva em arquivo
    for x in lista:
        saida.write("%i\n" %x) #escreve cada numero ordenado separado por linha
