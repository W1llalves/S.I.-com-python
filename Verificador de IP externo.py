# re -> permite operações com expressões regulares
# json -> fornece operações de codificação e decodificação json
# urllib.request import urlopen -> funções e classes que ajudam a abrir a url
# http://ipinfo.io/json

import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados ['org']
cidade = dados ['city']
pais = dados ['country']
regiao = dados ['region']

print("Detalhes do IP externo\n")
print("IP: {4}\nRegião: {1}\nCidade: {3}\nOrg: {0}".format(org, regiao, pais, cidade, ip))







