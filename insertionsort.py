# APA - Atividade 1 - InsertionSort
# Autor: Fábio Alexandre E. Melo
# Uso do Programa: insertionsort.py [Arquivo de Entrada] [Arquivo de Saida]

import sys # para fazer parsing dos argumentos

if len(sys.argv)< 2:
    print("ERRO - faltam argumentos. // Uso insertionsort.py [ENTRADA] [SAIDA]")
    exit()
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]
#   print(entrada)
#  print(saida)
    
lista = open(entrada, 'r').readlines() # abre o arquivo e salva cada linha como o elemento de uma lista (python é mágico!)

for x in range(0, len(lista)):  # loop para transformar a lista de strings em um array de inteiros. 
    lista[x] = int(lista[x])
    
for i in range (1, len(lista)):  # aqui é onde a ordenação acontece. começando de 1, pois não há necessidade de mexer com o primeiro item
    j = i;  # nossa variavel temporária j recebe do i, para fazer o loop decrescente.
  #  print("iteração de número " + str(i)) # print para fins de debugging
    while lista[j] < lista[j-1] and j > 0: # enquanto j for menor que o i e maior que 0, vai voltando posições e trocando os itens, caso sejam menores 
        lista[j], lista[j-1] = lista[j-1], lista[j] # outra mágica do python. diretamento fazendo a troca dos conteudos nas posições.
        j = j-1 # iterando até chegar em 0
 #       print(lista) # printando o caminho pra facilitar a visualização
            
print(lista) # printa a lista ordenada

with open(saida, 'w') as saida: #salvando em arquivo 
    for x in lista:
        saida.write("%i\n" %x) #escreve cada numero ordenado separado por linha

