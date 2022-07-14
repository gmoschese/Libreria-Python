#1. Creare un sistema di classi come specificato sotto:
# Animale, Felino, Canide, Uccello

class Animale():
    def __init__(self, nomeZooL):
        self.nome = nomeZooL

    def creaFelino(self, nomeL, razzaL, pesoL):
        return Felino(nomeL, razzaL, pesoL)

    def creaCanide(self, nomeL, razzaL, pesoL):
        return Canide(nomeL, razzaL, pesoL)

    def creaUccello(self, nomeL, razzaL, pesoL):
        return Uccello(nomeL, razzaL, pesoL)

    def getRazza(self):
        return self.razza
        #return Felino.__getRazza()

    def getPeso(self):
        return self.peso


class Felino(Animale):
    def __init__(self, nomeL, razzaL, pesoL):
        Animale.__init__(self, nomeL)
        self.razza = razzaL
        self.peso = pesoL

    """ def __getRazza(self):
        return self.razza """



class Canide(Animale):
    def __init__(self, nomeL, razzaL, pesoL):
        Animale.__init__(self, nomeL)
        self.razza = razzaL
        self.peso = pesoL


class Uccello(Animale):
    def __init__(self, nomeL, razzaL, pesoL):
        Animale.__init__(self, nomeL)
        self.razza = razzaL
        self.peso = pesoL



def __main1__():
    animale = Animale("safari")
    gatto = animale.creaFelino("aaa", "Pastore", 40)
    print(gatto.getPeso())


######################
#2 Crea una classe "DatiUtente" che derivi una classe figlia utente, i dati dell'utente devono essere inseriti 
# e richiesti nell'init del figlio, ma conservti nel padre. 
# Dev'essere possibile inserire quanti utenti si vuole e poi visualizzare la lista dei Nomi e se possiedi la PWD 
# tramite in nome anche accedere alla modifica della pwd

class Server:
    listaUtenti = {}

    def getUtenti(self):
        print("Gli utenti sono: ", Server.listaUtenti)

class DatiUtente(Server):
    def __init__(self, us, pwd):
        self.__username = us
        self.__password = pwd

    #def registration(self, us, pwd):
    #    self.__username = us
    #    self.__password = pwd
    
    

    def putUtente(self, usernameL):
        Server.listaUtenti.update({usernameL:self})


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


    

class Utente(DatiUtente):
    def __init__(self, us, pwd):
        DatiUtente.__init__(self, us, pwd)
        DatiUtente.putUtente(self, us)

    #def __init__(self, us, pwd):
    #    Sistema.__init__(self, us, pwd)
    
    def cambiaUSR(self, oldUSR, pwd, newUSR):
        DatiUtente.cambiaUSR(self, oldUSR, pwd, newUSR)

    def getInfoPrivate(self):
        usr = input("inserisci username: ")
        pwd = input("inserisci password: ")
        return DatiUtente.checkCredenziali(self, usr, pwd)
    
    def getInfoPrivate(self, usr, pwd):
        return DatiUtente.checkCredenziali(self, usr, pwd)
    
    def checkUsr(self, usr):
        return DatiUtente.checkUsermane(self, usr)
    
    def checkPsw(self, pwd):
        return DatiUtente.checkPassword(self, pwd)





def __main2_1__():
    giovanni = Utente("giovanni", "giovanni")

    print(giovanni.getInfoPrivate())


def __main2__():
    server = Server()
    giovanni = Utente("giovanni", "giovanni")
    giovanni.cambiaPWD("giovanni", "giovanni", "giovanni")
    server.getUtenti()



##################

#__main1__()
#__main2_1__()
__main2__()