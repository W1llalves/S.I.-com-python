#webbrowser -> fornece uma interface de alto nível para permitir a exibição de documentos web aos usuários
#tkinter -> fornece interface padrão do Python para o kit de ferramentas gráficas TK

import webbrowser
from tkinter import +

root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='abrir o Google' command=google).pack(pady=20)
root.mainloop()


