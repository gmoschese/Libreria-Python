# Esercizio sull'ereditarietà
#Parametri feeding lista:
# Nome
# Cognome
# Età
# Professione

from mailbox import NotEmptyError

class creaLista:

    def __init__(self):
        self.lista = []
    

listaDomande = ["Nome: ", "Cognome: ", "Età: ", "Professione: "]
oggetto = creaLista()
domanda = input(listaDomande[0])
if(type(domanda) == str):
    oggetto.lista.append(domanda)

domanda = input(listaDomande[1])
if(type(domanda) == str):
    oggetto.lista.append(domanda)

domanda = input(listaDomande[2])
if(type(int(domanda)) == int):
    oggetto.lista.append(domanda)

domanda = input(listaDomande[3])
if(type(domanda) == str):
    oggetto.lista.append(domanda)

print(oggetto.lista)