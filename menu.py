while True:  
    print("bevenuto nella nostra calcolatrice")
    print("inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1)sottrazione\n2)addizione\n0)exit\n"))

    if scelta==0:
        break
    elif scelta == 1:
       sottarzione()
    elif scelta== 2:
        Somma()
    else:
        print("scelta non corretta!")
