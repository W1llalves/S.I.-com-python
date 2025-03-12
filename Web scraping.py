#ferramenta de coleta de dados web, onde minera a extração de dados de sites webconvertendo informaçẽs estruturadas
# ... para posterior analise.

# BeautifulSoup ->  #biblioteca de extração de dados de arquivos HTML e XML
#requests -> #permie que você envie solicitações HTTP em python

from bs4 import beautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebe o conteúdo da requisição http do site...

soup = beautifulSoup(site, 'html.parser')
#objeto soup baixando do siteo html

print(soup.prettify)
#transforma html em string e o print vai exibir o html

temperatura = soup.find("span", class = "_block _margin-b-5 -gray")

print(temperatura.string)

print(soup.title.string)

print(soup.a)

print(soup.p.string)

print(soup.find('admin'))

-----------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

# Fazendo a requisição para a página de notícias
url = 'https://www.globo.com/'
response = requests.get(url)
html = response.text

# Criando o objeto Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Buscando todos os elementos que contêm os títulos das notícias
titulos = soup.find_all('h2', class_='post__title')

# Extraindo e imprimindo os títulos
for titulo in titulos:
    print(titulo.text.strip())








