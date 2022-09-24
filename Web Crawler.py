#ferramenta usada para encontrar, ler e indexar páginsa de um site. Utilizado para levantamento de informações em um pentest.

# BeautifulSoup ->  #biblioteca de extração de dados de arquivos HTML e XML
# operator -> #exporta um conjunto de funções eficientes correspondentesaos operadores intríncicos do python como:+-*/
# collections -> ajuda a preencher e manipula eficientemente as estruturas de dados como tuplas, dicionários e listas.

import requests
from bs4 import beautifulSoup, BeautifulSoup
import operator
from collections import counter




def start(url):

    wordlist = []
    #armazena toldo o conteúdo do site
    source_code = requests.get(url).text


    soup = BeautifulSoup(source_code, 'html.parser')

    # text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text    # procura no html todos os 'div' e 'class' colocando em um texto

        word = content.lower().split()   #colocar o texto em minusculo e separar as palavras por linhas

        for each_word in word:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%&*()-_=+[><:?];.,|\°º"

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '') #remover os simbolos encontrados

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}      #contagem de palavras

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
    print("% s : % s " % (key, value))        #mostrar as palras que mais aparecem no texto

    c = counter(word_count)


    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=lefbar")













