'''
Aula 9 - Orientação a objeto

#class
uma classe é uma descrição que abstrai um conjunto de objetos com características similares.
para exportar uma classe, utioliza-se:

    from aula9 import Pessoas

no exemplo acima o comando from esta buscando o arquivo 'aula9' e importando
de dentro dele a classe Pessoas
'''

from 9.1 import Pessoas

mariano = Pessoas('mariano', 18, 1.75) #DENTRO DAS ASPAS DEFINO OS VALORES QUE PARA AS VARIAVEIS EM PESSOAS

print(mariano)
print('Nome:', mariano.nome, '\nIdade:', mariano.idade, '\nTamanho:', mariano.tamanho)

#ENTÃO POSSO CRIAR UM PACOTE DE CODIGOS E EXPORTALOS PARA DENTO DE OUTRO CODIGO, UTILIZANDO class




