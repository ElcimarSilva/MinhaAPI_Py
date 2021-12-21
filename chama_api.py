import requests

link = ('https://minhaapi.elcimarsilva.repl.co/pegarvendas')

requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())