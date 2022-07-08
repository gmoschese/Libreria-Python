# Creare un input per scegliere che tipo di elemento essere

# Esercizio tipo 1 -> far si che, in base all'elemento scelto, il sistema mi richieda in input, tutte le caratteristiche necessarie 
    # per creare l'oggetto e poi stampare la lista delle sue proprietà

# Esercizio tipo 2 -> deve, per ogni inserimento iniziale, creare una lista che tiene a mente chi sono cosa

# Esercizio tipo 3 -> inserire un loop e far si che il processo si ripeterà x volte e alla fine stampi la 
    # somma di tutti i tipi



class persona:
    def __init__(self, nome, cognome, cf):
        self.Nome = nome
        self.Cognome = cognome
        self.CF = cf
    
    def stampaDettagliata(self):
        print(self.Nome, self.Cognome, self.CF)
    
    def stampaElenco(self):
        print(self.Nome, self.Cognome)


class studente(persona):
    def __init__(self, nome, cognome, cf, matricola):
        persona.__init__(self, nome, cognome, cf)
        self.Matricola = matricola
    
    def stampaDettagliata(self):
        print(self.Nome, self.Cognome, self.CF, self.Matricola)

class professore(persona):
    def __init__(self, nome, cognome, cf, matricola, stipendio):
        persona.__init__(self, nome, cognome, cf)
        self.Matricola = matricola
        self.Stipendio = stipendio
    
    def stampaDettagliata(self):
        print(self.Nome, self.Cognome, self.CF, self.Matricola, self.Stipendio)

class studenteScuolaSuperiore(studente):
    def __init__(self, nome, cognome, cf, matricola, flag=True):
        studente.__init__(self, nome, cognome, cf)
        self.Matricola = matricola
        self.Flag = flag
    
    def stampaDettagliata(self):
        print(self.Nome, self.Cognome, self.CF, self.Matricola, self.Flag)
    

ListaStudenti = []
ListaProfessori = []
ListaStudentiSuperiori = []

ListaTipi = ["Studente", "Professore", "Studente di scuola Superiore"]
listaDomandeStudente = ["Nome: ", "Cognome: ", "CF: ", "matricola: "]
listaDomandeProfessore = ["Nome: ", "Cognome: ", "CF: ", "matricola: ", "Stipendio: "]
listaDomandeStudenteScuolaSuperiore = ["Nome: ", "Cognome: ", "CF: ", "matricola: "]

for i in range(1):
    oggetto=""
    appartenenzaClasse = input("definizione della propria classe: ")
    print(appartenenzaClasse, ListaTipi[0].lower())
    if(appartenenzaClasse.lower() == ListaTipi[0].lower()): # Ramo Studente
        print("ramo studente", appartenenzaClasse)
        nome = input(listaDomandeStudente[0])
        cognome = input(listaDomandeStudente[1])
        cf = input(listaDomandeStudente[2])
        matricola = input(listaDomandeStudente[3])

        oggetto = studente(nome, cognome, cf, matricola)
        oggetto.stampaDettagliata()
        ListaStudenti.append(oggetto)


    if(appartenenzaClasse.lower() == ListaTipi[1].lower()): # Ramo Professore
        print("ramo professore", appartenenzaClasse)
        nome = input(listaDomandeProfessore[0])
        cognome = input(listaDomandeProfessore[1])
        cf = input(listaDomandeProfessore[2])
        matricola = input(listaDomandeProfessore[3])
        stipendio = input(listaDomandeProfessore[4])

        oggetto = professore(nome, cognome, cf, matricola, matricola, stipendio)
        oggetto.stampaDettagliata()
        ListaProfessori.append(oggetto)

    if(appartenenzaClasse.lower() == ListaTipi[1].lower()): # Ramo Studente di scuola superiore
        print("ramo studente superiore", appartenenzaClasse)
        nome = input(listaDomandeProfessore[0])
        cognome = input(listaDomandeProfessore[1])
        cf = input(listaDomandeProfessore[2])
        matricola = input(listaDomandeProfessore[3])

        oggetto = studenteScuolaSuperiore(nome, cognome, cf, matricola, matricola)
        oggetto.stampaDettagliata()
        ListaStudentiSuperiori.append(oggetto)

print("\n \n fine inserimento. Elenco dei registri:\n")
for i in ListaStudenti:
    print("Studente: ", end=" ") 
    i.stampaElenco()

for i in ListaProfessori:
    print("Studente: ", end=" ") 
    i.stampaElenco()

for i in ListaStudentiSuperiori:
    print("Studente: ", end=" ") 
    i.stampaElenco()
