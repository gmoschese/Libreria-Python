def prova4():
    messaggio1 = "siamo la classe migliore di "

    messaggio1Json = json.dumps(messaggio1)
    messaggio1Pickel = pickle.dumps(messaggio1)

    messaggio2 = {"a":11, "b":24, "c" : 11}

    messaggio2Json = json.dumps(messaggio2)
    messaggio2Pickel = pickle.dumps(messaggio2)

    flagGlobal = True

    while(flagGlobal):
        scelta1 = input("scegliere che tipo di conversione fare: Json [J] o Pickel[P]")
        if(scelta1 == "J"):
            messaggio1P = json.loads(messaggio1Json)
            print(messaggio1P)
            messaggio1P = messaggio1P + "Mai"
            nuovoMessaggioPickel = pickle.dumps(messaggio1P)
            print(nuovoMessaggioPickel)
            
            messaggio2P = json.loads(messaggio2Json)
            print(messaggio2P)
            messaggio2P["c"] = 232
            print(messaggio2P)
            nuovoMessaggio2Pickel = pickle.dumps(messaggio2P)
            print(nuovoMessaggio2Pickel)
            


        elif(scelta1 == "P"):
            messaggio1P = pickle.loads(messaggio1Pickel)
            messaggio1P = messaggio1P + "Mai"
            nuovoMessaggioJson = json.dumps(messaggio1P)
            print(nuovoMessaggioJson)

            messaggio2P = pickle.loads(messaggio2Pickel)
            print(nuovoMessaggio2Json)
            messaggio2P["c"] = 232
            nuovoMessaggio2Json = json.dumps(messaggio2P)
            print(nuovoMessaggio2Json)







def __main4__():
    prova4()

__main4__()
