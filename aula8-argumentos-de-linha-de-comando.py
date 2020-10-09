'''
Aula 8 - Bibliotecas e argumentos de linha de comando

#BIBLIOTECAS
é possivel no python importar uma bliblioteca. que são codigos já preescritos em potyhon, quando voce importa
essa biblioteca. assim é possivel utilizar mais metosdos dento do python. Pytonho possui algumas bibliotecas
que podem ser instalada atraves do comando:

import

#sys
É uma biblioteca que conversa com o sistema operacional, sendo possivel passar um argumento ao python
através do cmd.
'''

import sys

argumentos = sys.argv
print(argumentos)

def soma(a1, a2):
    return a1 + a2

def sub(a1, a2):
    return a1 - a2

if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]), float(argumentos[3]))

elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]), float(argumentos[2]))

print(resp)
