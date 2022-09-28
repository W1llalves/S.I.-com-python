# ctypes - fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou bibliotecas compartilhadas

import ctypes

pasta = input("Digie o caminho da pasta a ser ocultado. EXEMPLO:(C:/pasta/pasta1)")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttrbutesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado!!!")
else:
    print("Arquivo não foi ocultado!!!")







