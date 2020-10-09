'''
Aula 4 - Strings e Listas

#STRING
Uma string é como se denomina um texto no python. para se expressar uma string podesse utilizar 'x' ou "x".
Ou seja, tudo que tiver dentro de aspas ou de aspas deplas, será uma string.

No piton string é simplificada em srt

    Exemplo
    a = 'string'
        print(type(a))

    <class 'str'>



#LISTA
Uma lista é uma coleção, onde é possivel inserir diversas informações. para se expressar uma lista utiliza-se: []
Em python as contagens sempre começam do 0. Então, 0 1 2 3 4, são 5 digitos começando pelo 0.

Para separa os itens de uma uma lista (identar) utiliza-se: , ou +
A , da um espaço entre ela e a proxima letra. O + não da o espaçõ, juntando os dois caracteres.

    Exemple:
       

existem outros comados para modificar uma lista de diversas formas.

    lista = [1, 2]
    lista.clear() #.clear limpa toda a lista 
    print(lista)
[]

    lista.append('joao')
    print(lista)
['joao']
'''

lista_frutas = ['maça', 'pera', 'banana']
print(type(lista_frutas))
print('gosto muito de', lista_frutas[1]+'!')
       