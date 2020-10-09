'''
Aula 3 - Operadores lógicos e estruturas de decisões (IF e ELSE)

#DADO BOOLEAN OU BOLEANO (tipo)
Um dado tipo boolan possui apenas dois valores, True ou False.
Pode se estabeler valor bool a um objeto. >>> object = True ou >>> object = false


#EXTRUTURA DE DECISÃO.
if, corresponde ao 'se', então, se determinado parmetro corresponder com a extrutura solicitado no codigo,
ele executa a função. Por Exemplo:

    >>> a = True
    >>>if a == True:
    >>> print('a é igual a verdade')
    a é igual a verdade

    >>> c = 3
    >>> g = 4
    >>>if c + g = 7
    >>> print(c + g)
    7


else, corresponde a senão. Execute determinada função, senão, execute está.

    >>> a = 12
    >>> b = 24
    >>>if a > b:
    >>> print('a é miaor que b')
    >>>else:
    >>> print('a não é maior que b')
    a não é maior que b

elsif, coresponde a se/senão. se o python executar uma linha, não executara as proximas

    >>>if 1 + 2 = 4
    >>> print('ola pessoas')
    >>>elif 1 = 1
    >>> print('ola ola')
    >>>elif 1 + 2 = 3
    >>> print('isso ai')
    ola ola

vejamos que nesse caso ele printou o 'ola ola' e desistiu da proxima ação que tmb é verdadeira.



'''


'''
Exercicio: Faça um programa que pergunte a idade o peso e a altura de uma pessoa
e decide se ela esta apita a ser do exercito
para entrar no exercito é preciso ter meis ou igual a 18 anos, pesar mais de 60 quilos e medir mais de 1.70m
'''


print('PROGRAMA DE ADMISSÃO AO EXERCITO 1.0')
print('####################################')

nome = str(input('Digite seu nome:\n\n'))

print('Muito bem,', nome, '.')

idade = int(input('Quantos anos você possui?'))
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual su altura?'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Parabens!', nome, ', você possui todos os requisitos para servir ao exercito!')
else:
    print('Você não possui os requisitos para servir ao exercito!')