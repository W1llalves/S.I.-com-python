import whois
#WHOIS é um protocolo da pilha TCP/IP (porta 43) específico para consultar informações de contato e DNS sobre entidades na internet.

dominio = input ("ALVO: ")
consulta_whois = whois.whois(dominio)

#print consulta whois.name
print (consulta_whois)

'''
para instalar: baixe https://pypi.org/project/python-whois/
arraste para onde esta o python.exe e faca: python.exe setup.py install
'''
