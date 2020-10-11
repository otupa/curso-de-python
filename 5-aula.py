'''
Aula 5 - Estrutura de laço (while e for)

Em Python existem duas formas de criar uma estrutura de repetição:
O for é usado quando se quer iterar sobre um bloco de código um número determinado de vezes.
O while é usando quado queremos que o bloco de código seja repetido até que uma condição seja satisfeita.

'''

lista = ['mariano', 'joao', 'pedro']
for nome in lista:
    print(nome)
    

'''
No exemplo dois, enquanto o while não perceber que a é igual 4, ele ira dar print e somar 1 ao
valor de a, ate que seu valor se torne 4.
'''

a = 4
while a <= 0:
    print('a não é maior,', 'a é:', a)
    a += 1
