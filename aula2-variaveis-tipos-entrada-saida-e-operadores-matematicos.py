'''
Aula 2 - Variaveis, tipos, entrada, saida e operadores matemáticos

#ENTRADA E SAIDA
Entrada são os comandos dados ao python para que se execute determinada tarefa.
Saida é a resposta que é exibida no monitor.
Print é um comando usado para exibir uma informação na tela.


    *Exemplo1
        >>> print('ser ou não ser, eis a questão!') #entrada
        ser ou não ser eis a questão!               #saida

#VARIAVEL
Para criar uma variavel no python basta apenas especificar o nome da variavel e atribuir algun valor a ela.
O python utiliza o sinal de igual '=' para atribuir valores a variaveis.

    *Exemplo2
        >>> nome = julianan #VARIAVEL
        >>> print(nome)
        juliana

#TIPOS
Existem diferente tipos de objetos no pyton, entre eles.
    srt = string
    int = inteiro
    float = real

#OPERAÇÕES MATEMATICAS
O python pode processar operações matematicas utilizamdo os seguuintes simbolos:

    soma: +
    subtração: -
    dovisão: /
    muultiplicação: *
    Elevar ao quadrado: **
    Rair quadrada: ** (1/2)

#COMANDOS
    >>>input() #solcita uma informação na tela
    >>>print() #imprime uma informação na tela

'''
''''
EXERCICIO: Faça um formuilario que pergunte
o nome, cpf, endereço, idade, altura, e telefone.
E imprima isso em um relatorio organizado.
'''

print('Por favor, preencha este formulario!')

nome = input('Escreva seu nome: ')
cpf = input('Escreva seu CPF: ')
endereco = input('Escreva seu endereço: ')
idade = input('Escreva sua idade: ')
altura = input('Escreva sua altura: ')
telefone = input('Escreva seu telefone:')

print('\nFICHA DE CADASTRO')
print('Nome:', nome, '\ncpf:', cpf, '\nEndereço:', endereco, '\nIdade:', idade, '\nAltura:', altura, '\nTelefone:', telefone)
print()
print('FIM DO PROGRAMA!')
