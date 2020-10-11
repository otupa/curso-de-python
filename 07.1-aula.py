'''
Aula 7 - Funções e metodos

Exercicio:
Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro denta coleção
faça outra coleção que retorna o menor numero desta coleção
'''

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(maior([1, 2, 3, 4, 5, 6, 989, 342, 3]))

print(menor([1, 234, 578, 234,1233, 11]))
