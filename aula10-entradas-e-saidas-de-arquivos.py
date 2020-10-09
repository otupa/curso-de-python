'''
Aula10 - Entradas e Saidas de arquivos

É possivel abrir um arquivo com open()
a variavel open possui dois argumentos

    open('diretorio', 'metodo')
'''

#para abrir um arquivo txt
arquivo = open('Aula10.txt', 'w')

arquivo.write('eai pessoal, blz?')

'''
#METODO
    'r' = read ou leitura
    'w' = write ou escrever
    'r+' = read e write ou escrita e leitura
    'a' = append, adicionar ao final do arquivo
    'b' = bytes, arquivos que não são do tipo texto
'''