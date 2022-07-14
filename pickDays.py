class RiempiDict:
    def __init__(self):
        self.__dict = {}

    def addInDict(self, key, val):
        self.__dict.update({key: val})

    def printDic(self):
        print(self.__dict)

    def cancellaElemento(self, key):
        self.__dict.pop(key)




def __main1__():

    dic = RiempiDict()
    i = 0

    while i <= 5:
        k = input("inserisci chiave: ")
        v = input("inserisci valore: ")
        dic.addInDict(k, v)
        dic.printDic()
        i = i+1


def __main2__():
    dic = RiempiDict()

    dic.addInDict("nome", input("inserire nome: "))
    dic.addInDict("cognome", input("inserire cognome: "))
    dic.addInDict("eta", input("inserire eta: "))

    dic.printDic()

    keyToDel = input("inserire chiave da cancellare: ")


    dic.cancellaElemento(keyToDel)

    dic.printDic()

#############################################
class Sistema():

    def __init__(self, us, pwd):
        self.__username = us
        self.__password = pwd

    #def registration(self, us, pwd):
    #    self.__username = us
    #    self.__password = pwd
    
    def cambiaUSR(self, oldUSR, pwd, newUSR):
        if(oldUSR == self.__username and pwd == self.__password):
            self.__username = newUSR
        else:
            print("permesso negato")

    def cambiaPWD(self, USR, pwd, newPWD):
        if(USR == self.__username and pwd == self.__password):
            self.__password = newPWD
        else:
            print("permesso negato")
    
    def checkCredenziali(self, usr, pwd):
        if(usr == self.__username and pwd == self.__password):
            return "la risposta è 42"
        else:
            print("permesso negato")
            exit(1)

    def checkUsermane(self, usr):
        if(usr == self.__username):
            return True
        else:
            return False
    
    def checkPassword(self, pwd):
        if(pwd == self.__password):
            return True
        else:
            return False


    

class Utente(Sistema):
    def __init__(self, us, pwd):
        Sistema.__init__(self, us, pwd)

    #def __init__(self, us, pwd):
    #    Sistema.__init__(self, us, pwd)
    
    def cambiaUSR(self, oldUSR, pwd, newUSR):
        Sistema.cambiaUSR(self, oldUSR, pwd, newUSR)

    def getInfoPrivate(self):
        usr = input("inserisci username: ")
        pwd = input("inserisci password: ")
        return Sistema.checkCredenziali(self, usr, pwd)
    
    def getInfoPrivate(self, usr, pwd):
        return Sistema.checkCredenziali(self, usr, pwd)
    
    def checkUsr(self, usr):
        return Sistema.checkUsermane(self, usr)
    
    def checkPsw(self, pwd):
        return Sistema.checkPassword(self, pwd)





def __main3__():
    giovanni = Utente("giovanni", "giovanni")

    print(giovanni.getInfoPrivate())


def __main4__():
    giovanni = Utente("giovanni", "giovanni")
    i = 0
    max = 3
    while(i < max):
        username = input("inserire username: ")
        if(not giovanni.checkUsr(username)):
            i = i + 1
            print("username errato, riprova", i,"/", max)
        else:
            j = 0 
            i = 3
            while(j < max):
                print("ddd")
                password = input("inserire password: ")
                if(not giovanni.checkPsw(password)):
                    j = j + 1
                    print("password errata, riprova", j,"/", max)
                else:
                    giovanni.getInfoPrivate(username, password)
                    

####################################
def __main5__():
    listaNomi = ["giovanni", "mirko"]
    listaCognomi = ["moschese", "campari"]

    for i in range(1):
        for i in range(len(listaCognomi)):
            print(listaNomi[i], listaCognomi[i])


    for i in listaNomi: 
        for j in listaCognomi:
            print(i, end=" ")
            print(j)
            
########################################
class Squadra:
    def __init__(self, giocatori):
        self.listaSquadra = []
        if len(giocatori) == 5:
            for i in giocatori:
                self.listaSquadra.append(i)

    def cambioGiocatore(self, giocatoreIn, giocatoreOut):
        self.listaSquadra.remove(giocatoreOut)
        self.listaSquadra.append(giocatoreIn)

    def contaGiocatoriSquadra(self):
        return len(self.listaSquadra)
    
    def elencaSquadra(self):
        for i in self.listaSquadra:
            print(i.nome, i.cognome, i.maglia)

class Giocatore:
    def __init__(self, nomeY, cognomeY, magliaY):
        self.nome = nomeY
        self.cognome = cognomeY
        self.maglia = magliaY

def __main6__():
    giocatore1 = Giocatore("a", "aa", 1)
    giocatore2 = Giocatore("b", "bb", 2)
    giocatore3 = Giocatore("c", "cc", 3)
    giocatore4 = Giocatore("d", "dd", 4)
    giocatore5 = Giocatore("e", "ee", 5)
    giocatore6 = Giocatore("f", "ff", 6)
    giocatore7 = Giocatore("g", "gg", 7)
    giocatore7 = Giocatore("h", "hh", 8)

    squadaIniziale = [giocatore1,giocatore2,giocatore3,giocatore4, giocatore5]
    squadra = Squadra(squadaIniziale)

    print(squadra.contaGiocatoriSquadra())

    squadra.elencaSquadra()
    squadra.cambioGiocatore(giocatore6, giocatore1)
    print(squadra.contaGiocatoriSquadra())
    squadra.elencaSquadra()



##########################
class Comune:
    def __init__(self):
        self.__budget = 0
        self.__perASL = 0
        self.__perProloco = 0
        self.__perComune = 0
        self.__budProloco = 0
        self.__budASL = 0
        self.__budComune = 0
        
    def riassegnaBudget(self, budgetY, perASLy, perProlocoY, perComuneY):
        if((perASLy + perProlocoY + perComuneY) == 100):
            self.__budget = budgetY
            self.__perASL = perASLy
            self.__perProloco = perProlocoY
            self.__perComune = perComuneY
            self.__budProloco = self.__budget * (self.__perProloco / 100)
            self.__budASL = self.__budget * (self.__perASL / 100)
            self.__budComune = self.__budget * (self.__perComune / 100)
            print(self.__budASL)
        else:
            print("errore")
            exit(1)

    def getBudComune(self):
        return self.__budComune

    def getBudProloco(self):
        return self.__budProloco

    def getBudASL(self):
        return self.__budASL

class ASL(Comune):
    def __init__(self):
        Comune.__init__(self)
        self.budget = 0

    def setBudget(self):
        self.budget = Comune.getBudASL(self)
        
class Proloco(Comune):
    def __init__(self):
        Comune.__init__(self)
        self.budget = 0

    def setBudget(self):
        self.budget = Comune.getBudProloco(self)




    
def __main7__():
    milano = Comune()
    milano.riassegnaBudget(100, 60, 20, 20)
    sanita = ASL()
    cultura = Proloco()

    sanita.setBudget()
    print(sanita.budget)

##################################
class Ospedale_Old:
    registro = {}
    def __init__(self, nomeY, cittaY):
        self.nome = nomeY
        self.citta = cittaY
        

    def insertimentoOre(self, matricola, ore):
        Ospedale.registro.update({matricola : ore})

    def printOre(self):
        print(self.registro)

    def resetRegistro(self):
        self.registro.clear

class Dottore_OLD(Ospedale_Old):
    def __init__(self, nomeY, cittaY, matricolaY):
        Ospedale.__init__(self, nomeY, cittaY)
        self.matricola = matricolaY

    def insertOre(self, ore):
        Ospedale.insertimentoOre(self, self.matricola, ore)
        

class Specialista_OLD(Dottore_OLD):
    def __init__(self, nomeY, cittaY, matricolaY, specializzazioneY):
        Dottore.__init__(self, nomeY, cittaY, matricolaY)
        self.specializzazione = specializzazioneY

def __main8__():
    ospedale = Ospedale("San Raffaele", "Milano")
    generico = Dottore("Rossi", "Milano", "DOTT01")
    specialista = Specialista_OLD("Bianchi", "Milano", "SPEC001", "Cardiolodo")

    generico.insertOre(4)

    specialista.insertOre(5)

    ospedale.printOre()
    generico.printOre()
    specialista.printOre()

class Ospedale:
    def __init__(self):
        self.registroOre = {}


class Dottore:
    def __init__(self, nomeL, cognomeL, matricolaL):
        self.nome = nomeL
        self.cognome = cognomeL


############################################
class Fabbrica:
    def __init__(self, nomeL, cittaL):
        self.nome = nomeL
        self.citta = cittaL
        #self.produzione = produzioneL

    def creaFabbricaVespa(self, nomeL, cittaL):
        return FabbricaVespa(self, nomeL, cittaL)

    def creaFabbricaZip(self, nomeL, cittaL):
        return FabbricaZip(self, nomeL, cittaL)


    def creaFabbricaLibery(self, nomeL, cittaL):
        return FabbricaLiberty(self, nomeL, cittaL)

    def introYourSelf(self):
        print(self.produzione)


class FabbricaLiberty(Fabbrica):
    def __init__(self, nomeL, cittaL, produzioneL):
        Fabbrica.__init__(self, nomeL, cittaL)
        self.produzione = "Liberty"
    


class FabbricaZip(Fabbrica):
    def __init__(self, nomeL, cittaL, produzioneL):
        Fabbrica.__init__(self, nomeL, cittaL)
        self.produzione = "SR"

class FabbricaVespa(Fabbrica):
    def __init__(self, nomeL, cittaL, produzioneL):
        Fabbrica.__init__(self, nomeL, cittaL)
        self.produzione = "Vespa"

def __main9__():
    fabbrica = Fabbrica("piaggio", "aprilia")

    fabbricaVespa = fabbrica.creaFabbricaVespa("PiaggioVespa", "Milano")
    fabbricaVespa.introYourSelf()

    fabbricaZip = fabbrica.creaFabbricaZip("PiaggioVespa", "Milano")
    fabbricaZip.introYourSelf()

    fabbricaLiberty = fabbrica.creaFabbricaLibery("PiaggioVespa", "Milano")
    fabbricaLiberty.introYourSelf()
#################################################################
class Fabbrica:
    def __init__(self, nomeL, cittaL):
        self.nome = nomeL
        self.citta = cittaL
        #self.produzione = produzioneL

    def creaFabbricaVespa(self, nomeL, cittaL):
        return FabbricaVespa(self, nomeL, cittaL)

    def creaFabbricaZip(self, nomeL, cittaL):
        return FabbricaZip(self, nomeL, cittaL)


    def creaFabbricaLibery(self, nomeL, cittaL):
        return FabbricaLiberty(self, nomeL, cittaL)

    def introYourSelf(self):
        print(self.produzione)


class FabbricaLiberty(Fabbrica):
    def __init__(self, nomeL, cittaL, produzioneL):
        Fabbrica.__init__(self, nomeL, cittaL)
        self.produzione = "Liberty"
    


class FabbricaZip(Fabbrica):
    def __init__(self, nomeL, cittaL, produzioneL):
        Fabbrica.__init__(self, nomeL, cittaL)
        self.produzione = "SR"

class FabbricaVespa(Fabbrica):
    def __init__(self, nomeL, cittaL, produzioneL="Vespa"):
        Fabbrica.__init__(self, nomeL, cittaL)
        self.produzione = produzioneL 
    
    def creaFabbricaPulegiaVespa(self, nomeL, cittaL):
        return FabbricaPulegiaVespa(self, nomeL, cittaL)
        


class FabbricaPulegiaVespa(FabbricaVespa):
    def __init__(self, nomeL, cittaL, produzioneL):
        FabbricaVespa.__init__(self, nomeL, cittaL, produzioneL)
        self.produzione = "pulegia Vespa"

def __main10__():
    fabbrica = Fabbrica("piaggio", "aprilia")

    fabbricaVespa = fabbrica.creaFabbricaVespa("PiaggioVespa", "Milano")
    fabbricaVespa.introYourSelf()

    fabbricaZip = fabbrica.creaFabbricaZip("PiaggioVespa", "Milano")
    fabbricaZip.introYourSelf()

    fabbricaLiberty = fabbrica.creaFabbricaLibery("PiaggioVespa", "Milano")
    fabbricaLiberty.introYourSelf()

    fabbricaPulegiaVespa = fabbricaVespa.creaFabbricaPulegiaVespa("PulegieVespaPiaggio", "Roma")
    print(fabbricaPulegiaVespa.nome, fabbricaPulegiaVespa.citta, fabbricaPulegiaVespa.produzione)
    fabbricaPulegiaVespa.introYourSelf()




#__main1__()
#__main2__()
#__main3__()
#__main4__()
#__main5__()
#__main6__()
#__main7__()
#__main8__()
#__main9__()
__main10__()

