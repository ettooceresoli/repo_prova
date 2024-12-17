while True:  
    print("bevenuto nella nostra calcolatrice")
    print("inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1)sottrazione\n2)addizione\n0)exit\n"))

    if scelta==0:
        break
    elif scelta == 1:
        n1= int(input("inserisci il primo numero"))
        n2= int(input("inserisci il secondo numero"))
        print(f"{n1}-{n2}={n1-n2}")
    elif scelta== 2:
        n1= int(input("inserisci il primo numero"))
        n2= int(input("inserisci il secondo numero"))
        print(f"{n1}+{n2}={n1+n2}")
    else:
        print("scelta non corretta!")