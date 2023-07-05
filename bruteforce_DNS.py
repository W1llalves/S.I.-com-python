#baixar pip e dnspython na maquina linux

import dns.resolver

res = dns.resolver.Resolver()
alvo = "127.0.0.1"

try:     #o codigo não vai parar em caso de erro
    resultado = res.resolve(alvo, "A")
    for ip in resultado:
        print(alvo, "->", ip)

except:
        pass  #ignorar