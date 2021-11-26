#	Napravite rječnik koji će čuvati ime i prezime studenta pod ključem koji je njegov JMBAG.
#   Na smislen način omogućite korisniku dvije operacije: unos novog zapisa te pretraživanje po JMBAG-u.
#   Nakon svake obavljene operacije pitajte korisnika želi li dalje i ponavljajte dok to korisnik želi.



rijecnik = {}

def UNOS():
    while True:
        IME = input("Unesi ime i prezime: ")
        JMBAG = input("Unesi JMBAG kljuc: ")
        rijecnik[JMBAG] = IME
        odb = input("Zelite li jos unosa? d/n: ")
        if odb != "d": 
            break
        else: 
            continue
    print(rijecnik)

def PRETRAZI():
    while True:
        pretrazi = input("Unesi JMBAG za pretrazivanje baze: ")
        a = print(rijecnik[pretrazi])
        odb = input("Želite li pretražiti još? d/n")
        if odb != "d":
            return a
        else: continue
    
while True:
    odabir = input("1 - Unesi podatak\n2 - Pretrazi podatak\n3 - Izađi\n")
    if odabir == "1":
        UNOS()
    elif odabir == "2":
        PRETRAZI()
    else: 
        break