import json 

def prova1():
    listaDatiRicevuti = []
    messaggioPy1 = {

    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
    ]
    }

    messaggioPy2 = ["a", "b"]
    messaggioPy3 = { "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("CCC","BBBB"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 20},
    {"model": "Ford Edge", "mpg": 22}
    ]
    }

    flag = True
    conversionePtoJ = ""
    while(flag == True):
        scelta1 = input("Buongiorno, cosa vuoi fare? Ricevere (Loads [L]), Inviare (Dump [D]), o Uscire (END)")
        if(scelta1 == "L"):
            if(len(listaDatiRicevuti) == 0 ):
                print("dati non presenti in cache, caricare prima ;-) ")
            else:
                print(("sono presenti ", len(listaDatiRicevuti), " dati, quale scegliere? Ricordati di partire da 0 ;-)"))
                scelta2 = input("")
                if(int(scelta2) < len(listaDatiRicevuti)):
                    messaggioJson= listaDatiRicevuti[int(scelta2)]
                    conversioneJtoP = json.loads(messaggioJson)
                    print(conversioneJtoP)
        elif(scelta1 == "D"):
            scelta3 = input("scegliere quale messaggio inviare: [1,2,3]")
            if(scelta3 == "1"):
                print("carico primo dato")
                conversionePtoJ = json.dumps(messaggioPy1, indent=4)
                listaDatiRicevuti.append(conversionePtoJ)
            elif(scelta3 == "2"):
                print("carico primo dato")
                conversionePtoJ = json.dumps(messaggioPy2, indent=4)
                listaDatiRicevuti.append(conversionePtoJ)
            elif(scelta3 == "3"):
                print("carico primo dato")
                conversionePtoJ = json.dumps(messaggioPy3, indent=4)
                listaDatiRicevuti.append(conversionePtoJ)
            elif(scelta3 == "END"):
                flag = False
            else:
                print("scelta sbagliata")
        elif(scelta1 == "END"):
            flag = False


        else:
            print("scelta sbagliata")

def prova2():
    
    listaDatiRicevuti = []
    flagGlobal = True
    conversionePtoJ = ""
    insertMulty = True
    while(flagGlobal):
        scelta1 = input("Buongiorno, cosa vuoi fare? Ricevere (Loads [L]), Inviare (Dump [D]), o Uscire (END)")
        if(scelta1 == "L"):
            if(len(listaDatiRicevuti) == 0 ):
                print("dati non presenti in cache, caricare prima ;-) ")
            else:
                flagLoad = True
                while(flagLoad):
                    print(("sono presenti ", len(listaDatiRicevuti), " dati, quale scegliere? Ricordati di partire da 0, altrimenti END per uscire ;-)"))
                    scelta2 = input("")
                    if(scelta2 == "END"):
                        flagLoad = False
                    elif(int(scelta2) < len(listaDatiRicevuti)):
                        messaggioJson= listaDatiRicevuti[int(scelta2)]
                        conversioneJtoP = json.loads(messaggioJson)
                        print(conversioneJtoP)
        elif(scelta1 == "D"):
            flagDump = True
            while(flagDump):
                scelta2 = input("continuare ad inserire? [Y/N")
                if(scelta2 == "Y" and insertMulty):
                    partecipante = input("Inserisci matricola dei partecipanti") 
                    listaDatiRicevuti.append(partecipante)
                elif(scelta2 == "N"):
                    flagDump = False
                    json.dumps(listaDatiRicevuti)
                    print(listaDatiRicevuti)

        elif(scelta1 == "END"):
            flagGlobal = False

def __main1__():
    prova2()


__main1__()


def prova3():
    
    listaDatiRicevuti = []
    flagGlobal = True
    insertMulty = True
    while(flagGlobal):
        scelta1 = input("Buongiorno, cosa vuoi fare? Ricevere (Loads [L]), Inviare (Dump [D]), o Uscire (END)")
        if(scelta1 == "L"):
            if(len(listaDatiRicevuti) == 0 ):
                print("dati non presenti in cache, caricare prima ;-) ")
            else:
                flagLoad = True
                while(flagLoad):
                    print(("sono presenti ", len(listaDatiRicevuti), " dati, quale scegliere? Ricordati di partire da 0, altrimenti END per uscire ;-)"))
                    scelta2 = input("")
                    if(scelta2 == "END"):
                        flagLoad = False
                    elif(int(scelta2) < len(listaDatiRicevuti)):
                        messaggioJson= listaDatiRicevuti[int(scelta2)]
                        conversioneJtoP = json.loads(messaggioJson)
                        print(conversioneJtoP)
        elif(scelta1 == "D"):
            flagDump = True
            while(flagDump):
                scelta2 = input("continuare ad inserire? [Y/N/M]")
                if(scelta2 == "Y" and insertMulty):
                    partecipante = input("Inserisci matricola dei partecipanti") 
                    listaDatiRicevuti.append(partecipante)
                elif(scelta2 == "M" and insertMulty) :
                    insertMulty = False
                    flagDump = False
                    partecipanti = input("Inserisci lista di matricole dei partecipanti: es m1,m2,m3") 
                    for i in partecipanti.split(","):
                        listaDatiRicevuti.append(i)
                elif(scelta2 == "N"):
                    flagDump = False
                    json.dumps(listaDatiRicevuti)
                    print(listaDatiRicevuti)
        elif(scelta1 == "END"):
            flagGlobal = False
def __main2__():
    prova3()


#__main2__()







