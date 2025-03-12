#baixar pip e dnspython na maquina linux

import dns.resolver

res = dns.resolver.Resolver()
alvo = "google.com"

try:     #o codigo não vai parar em caso de erro
    resultado = res.resolve(alvo,"A")
    for ip in resultado:
        print(alvo, "->", ip)

except dns.resolver.NoAnswer:
    print(f"Sem resposta para {alvo}")
except dns.resolver.NXDOMAIN:
    print(f"Domínio {alvo} não encontrado")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
