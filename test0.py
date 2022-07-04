# Consegna: 
# 1. Creare un sistema che prenda in input un dato e lo stampi dopo aver controllato che non abba valore False
# 2. Creare una serie di input inserirli in una lista e stamparli, controllando che non abbia valori False 
# 3. Creare un sistema di domande e input che inseriscano e controllino i dati, se non sono corretti non verranno inseriti nella lista



#1#2#3
ListOfAnsware=[]
ListOfAllowedAnsware=["Napoli", "20", "Matematica", "Bologna"]
domanda1="da dove vieni?"
domanda2="quanti anni hai?"
domanda3="cosa studi?"
domanda4="Dove"

risposta1= input(domanda1)
if(domanda1 and risposta1.lower() == ListOfAllowedAnsware[0].lower()):
    print(risposta1)
    ListOfAnsware.append(risposta1)

risposta2= input(domanda2)
if(domanda2 and int(risposta2) >= int(ListOfAllowedAnsware[1])):
    print(risposta2)
    ListOfAnsware.append(risposta2)

risposta3= input(domanda3)
if(domanda3 and risposta3.lower() == ListOfAllowedAnsware[2].lower()):
    print(risposta3)
    ListOfAnsware.append(risposta3)

risposta4= input(domanda4)
if(domanda4 and risposta4.lower() == ListOfAllowedAnsware[3].lower()):
    print(risposta4)
    ListOfAnsware.append(risposta4)

print(ListOfAnsware)