'''
Aula 12 - Bibliotecas, pip e requisições

pip é o comando usado para instalar determinadas bibliotecas.
O pacote request permite solicitar informações de um endereço web.

requests.get('') pedir informações ao site
requests.post('') postar informação

cabeçalho
'''

import requests

requisicao = requests.get('https://github.com/MarianoTupa/curso-de-python')

print(requisicao.text)

