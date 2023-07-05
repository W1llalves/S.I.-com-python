#"alvo.com.br" nome do dominio alvo
#80 -> numero da porta
# "b" converte o que estiver entre aspas em bytes

import socket

ports = {21, 22, 80, 8080, 443, 445, 3306, 25, 993}

for port in ports:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)  #quantidade de tempo de espera de resposta
    code = client.connect_ex(("alvo.com.br", port))
    #print(code) #caso a resposta seja zero ocorre conexão

    if code == 0:
        print(port, " aberta")
    else:
        print(port, " fechada.")


#caso queira se comunicar (trocar informações) com o servidor alvo:
#resposta = client.recv(1024) #recebe dados (1024) quantidade de bytes
#print(resposta.decode())  ##.decode converte a resposta em string
