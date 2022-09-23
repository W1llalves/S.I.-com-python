import hashlib

arquivo1 = 'a1.txt'
arquivo2 = 'a2.txt'

hash1 = hashlib.new('md5')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('md5')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(format(f'O Arquivo {arquivo1} é diferente do arquivo {arquivo2} !!!'))
    print(f'O hash do arquivo {arquivo1} é :', hash1.hexdigest())
    print(f'O hash do arquivo {arquivo2} é :', hash2.hexdigest())
else:
    print(format(f"O arquivo: {arquivo1} é igual ao arquivo: {arquivo2} !!!"))
    print(f'O hash do arquivo {arquivo1} é :', hash1.hexdigest())
    print(f'O hash do arquivo {arquivo2} é :', hash2.hexdigest())





