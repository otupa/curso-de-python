

print('programa de controle da festa 1.0') 
print('#################################') 

numero_convidados = input('Coloque o numero de convidados: ') 
lista_convidados = [] 

i = 1 

while i <= int(numero_convidados): 
    nome_convidado = input('Digite o nome do convidado: '+ str(i) + ':') 
    i += 1 
    lista_convidados.append(nome_convidado) 
    print('\n', 'LISTA DE CONVIDADOS') 
    print('Serão', numero_convidados, 'convidados na festa.') 
for nome in lista_convidados: 
    print(nome)