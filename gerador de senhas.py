import random
import string

print('Segundo as boas práticas de segurança da informação são necessário no mínimo 16 caracteres!')
tamanho = input("Qual o tamnho da senha que deseja gerar? :")                     #tamanho da senha

chars = string.ascii_letters + string.digits + 'çÇ!@#$%&*()?/|*-+._='        #estrutura da senha que será gerada (maiusculas e minusculos, numeros e caracters)

rnd = random.SystemRandom()

print('Senha gerada de forma randômica incluindo: MAIÚSCULA, minúscula, num3r1c4 e Ç@r@çt&r&$ ')
print('-'*30 + 'Nova Senha' + '-'*30)
print(' '*30 + ''.join(rnd.choice(chars) for i in range (int(tamanho))))
print('-'*70)











