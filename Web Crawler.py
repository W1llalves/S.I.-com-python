#ferramenta usada para encontrar, ler e indexar páginsa de um site. Utilizado para levantamento de informações em um pentest.

# BeautifulSoup ->  #biblioteca de extração de dados de arquivos HTML e XML
# operator -> #exporta um conjunto de funções eficientes correspondentesaos operadores intríncicos do python como:+-*/
# collections -> ajuda a preencher e manipula eficientemente as estruturas de dados como tuplas, dicionários e listas.

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter




def start(url):

    wordlist = []
    #armazena toldo o conteúdo do site
    source_code = requests.get(url).text


    soup = BeautifulSoup(source_code, 'html.parser')

    # text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
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

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))        #mostrar as palras que mais aparecem no texto

    c = counter(word_count)


    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=lefbar")



------------------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

target_url = "https://www.scrapingcourse.com/ecommerce/"

# initialize the list of discovered URLs
urls_to_visit = [target_url]

# set a maximum crawl limit
max_crawl = 20

def crawler():
    # set a crawl counter to track the crawl depth
    crawl_count = 0

    while urls_to_visit and crawl_count < max_crawl:

        # get the page to visit from the list
        current_url = urls_to_visit.pop()

        # request the target URL
        response = requests.get(current_url)
        response.raise_for_status()
        # parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # collect all the links
        link_elements = soup.select("a[href]")
        for link_element in link_elements:
            url = link_element["href"]

            # convert links to absolute URLs
            if not url.startswith("http"):
                absolute_url = requests.compat.urljoin(target_url, url)
            else:
                absolute_url = url

            # certifique-se de que o link rastreado pertence ao domínio de destino e não foi visitado
            if (
                absolute_url.startswith(target_url)
                and absolute_url not in urls_to_visit
            ):
                urls_to_visit.append(absolute_url)

            # update the crawl count
            crawl_count += 1

    # print the crawled URLs
    print(urls_to_visit)

# execute the crawl
crawler()









