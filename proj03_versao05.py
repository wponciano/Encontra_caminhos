
def identifica_rio(linha, coluna,tamanho_rio = 0,tamanho_terra = 0):
    # Vai substituir 1 por R e colocar o primeiro valor unitário para comprimento do rio
    if matrix_original[linha][coluna] == 1:  
        matrix_original[linha][coluna] = 'R' #vai mudar de 1 para R, com isso deixa de olhar para ele ao rodar por elementos já vistos
        tamanho_rio += 1  # vai registrar o comprimento do rio
        tamanho_rio = checa_vizinhos(linha,coluna, tamanho_rio,tamanho_terra)
    return tamanho_rio

def identifica_terra(linha, coluna,tamanho_rio=0,tamanho_terra = 0):
    if matrix_original[linha][coluna] == 0:  
        matrix_original[linha][coluna] = 'T' 
        tamanho_terra += 1  
        tamanho_terra = checa_vizinhos(linha,coluna, tamanho_rio,tamanho_terra)
    return tamanho_terra
    
def checa_vizinhos(linha, coluna, tamanho_atualizado_rio,tamanho_atualizado_terra): 
    # Vai olhar se os vizinhos são rios e atualizar o comprimento do rio

    if linha > 0:  # checa linha de cima
        tamanho_atualizado_rio = identifica_rio(linha-1,coluna,tamanho_atualizado_rio)
        tamanho_atualizado_terra = identifica_terra(linha-1,coluna,tamanho_atualizado_terra)
    
    if linha < qtde_linhas-1: # checa linha de baixo
        tamanho_atualizado_rio = identifica_rio(linha+1,coluna,tamanho_atualizado_rio)
        tamanho_atualizado_terra = identifica_terra(linha+1,coluna,tamanho_atualizado_terra)

    if coluna > 0:  # checa coluna esquerda
        tamanho_atualizado_rio = identifica_rio(linha,coluna-1,tamanho_atualizado_rio)
        tamanho_atualizado_terra = identifica_terra(linha,coluna-1,tamanho_atualizado_terra)

    if coluna < qtde_colunas-1:  # checa coluna direita
        tamanho_atualizado_rio = identifica_rio(linha,coluna+1,tamanho_atualizado_rio)
        tamanho_atualizado_terra = identifica_terra(linha,coluna+1,tamanho_atualizado_terra)

    return tamanho_atualizado_rio,tamanho_atualizado_terra

'''def checa_vizinhos_terra(linha, coluna, tamanho_atualizado_terra): 
    
    if linha > 0:  # checa linha de cima
        tamanho_atualizado_terra = identifica_terra(linha-1,coluna,tamanho_atualizado_terra)
    
    if linha < qtde_linhas-1: # checa linha de baixo
        tamanho_atualizado_terra = identifica_terra(linha+1,coluna,tamanho_atualizado_terra)

    if coluna > 0:  # checa coluna esquerda
        tamanho_atualizado_terra = identifica_terra(linha,coluna-1,tamanho_atualizado_terra)

    if coluna < qtde_colunas-1:  # checa coluna direita
        tamanho_atualizado_terra = identifica_terra(linha,coluna+1,tamanho_atualizado_terra)

    return tamanho_atualizado_terra'''

def acha_rio(matrix):  # função principal, chama as demais funções

    for linha in range(0,qtde_linhas): # corre todas as linhas
        for coluna in range(0,qtde_colunas): # corre todas as colunas
            if matrix[linha][coluna] == 1:
                retorno = identifica_rio(linha,coluna)
                lista_rio_final.append(retorno)
    return lista_rio_final

def acha_terra(matrix):  # função principal, chama as demais funções

    for linha in range(0,qtde_linhas): # corre todas as linhas
        for coluna in range(0,qtde_colunas): # corre todas as colunas
            if matrix[linha][coluna] == 0:
                retorno = identifica_terra(linha,coluna)
                lista_terra_final.append(retorno)
    return lista_terra_final                    

lista_rio_final = []
lista_terra_final =[]

#Gerador automático de matriz

import random

num_linhas = int(input('Entre com o número de linhas: '))
num_colunas = int(input('Entre com o número de colunas: '))

lista_linha =[]
matrix_original=[]


for linha in range(0,num_linhas):
    for coluna in range(0,num_colunas):
        lista_linha.append(random.randint(0,1))
    matrix_original.append(lista_linha)
    lista_linha=[]

print('##########   Matriz de Entrada   #############')

print(matrix_original)


qtde_linhas = len(matrix_original) # vai printar a qtde de elementos na lista
qtde_colunas = len(matrix_original[0])# vai printar a qtde de elementos na coluna-considerando que todas as linhas tem a mesma qtde de colunas


print('Qtde de linhas da matriz:',len(matrix_original))  # vai printar a qtde de elementos na lista
print('Qtde de colunas da matriz:',len(matrix_original[0])) # vai printar a qtde de elementos na coluna - considerando que todas as linhas tem a mesma qtde de colunas

decisao = input('Deseja localizar Terra ou Rio? T ou R: ').upper()

if decisao == "R":
    print("#############    RESULTADOS MATRIZ    ###################")

    qtde_total_rios = acha_rio(matrix_original)
    print('Qtde de rios encontrada:',len(qtde_total_rios))
    print('Lista de comprimentos dos rios:',acha_rio(matrix_original))

elif decisao == "T":
    print("#############    RESULTADOS MATRIZ    ###################")

    qtde_total_terra = acha_terra(matrix_original)
    print('Qtde de terras/ilhas encontrada:',len(qtde_total_terra))
    print('Lista de comprimentos das terras/ilhas:',acha_terra(matrix_original))

else:
    print('Valor de entrada inválido! Tente novamente com \'T\' para terra ou \'R\' para rio')            
        
