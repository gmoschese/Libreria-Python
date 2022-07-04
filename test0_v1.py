# Consegna: 
# 1. Creare un sistema che prenda in input un dato e lo stampi dopo aver controllato che non abba valore False
# 2. Creare una serie di input inserirli in una lista e stamparli, controllando che non abbia valori False 
# 3. Creare un sistema di domande e input che inseriscano e controllino i dati, se non sono corretti non verranno inseriti nella lista



#1#2#3
#Metodo alternativo:
ListOfAnsware=[]
questions = ["Da dove vieni?", "Quanti anni hai?","Cosa studi?", "Dove", "Perché?"]
ListOfAllowedAnsware=["Napoli", "20", "Matematica", "Bologna", "Mi piace"]
for x in range(len(questions)):
    risposta = input(questions[x])
    if(risposta and risposta.lower() == ListOfAllowedAnsware[x].lower()):
        print(risposta)
        ListOfAnsware.append(risposta)

print(ListOfAnsware)