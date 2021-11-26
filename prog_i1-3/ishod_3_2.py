#	Napišite program koji „zamisli” slučajni broj između 1 i 100.
#   Neka korisnik zatim pogađa broj, a vi mu nakon svakog pokušaja ispišite je li pogodio, podbacio ili prebacio.
#   Ispišite na kraju iz koliko pokušaja je pogodio. Koristite funkcije prema potrebi (morate imati najmanje jednu).
import random

r = random.randint(1, 100)

def funkc(r):
    flag = False
    count = 1
    while flag == False: 
        u = int(input("Unesi broj od 1 od 100: "))
        if u < r:
            print("Unos je podbacio")
            flag = False
            count += 1
        elif u > r:
            print("Unos je prebacio")
            flag = False
            count += 1
        elif u == r: 
            print("Broj je pogođen!!")
            flag = True
            print("Ukupni broj pokušaja: {}".format(count))

funkc(r)