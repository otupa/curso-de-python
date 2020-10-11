'''
Aula 11 - Tratamento de erros e exceções

para rodar um codigo e o programa não parar utilizasse try e except.

no exemplo abaixo 1 não pode ser dividido por 0,
então o python retorna erro ZeroDivisionError: division by zero

    a = 1/0
    print(a)

    a = 1/0
ZeroDivisionError: division by zero        #erro
'''

#utilizando try e except

try:
    a = 1/0
    print(a)
except:
    print('divisão por zero não da')


