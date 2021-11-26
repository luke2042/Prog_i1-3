#	Napišite funkciju koja prima četiri broja a, b, c i d.
#   Neka funkcija vrati najveći od proslijeđenih brojeva.
#   U glavnoj funkciji učitajte od korisnika četiri broja i pozovite funkciju, te ispišite vraćenu vrijednost.

def funkc(a, b, c, d):
    return max(a, b, c, d)

br1 = int(input("Unesi broj za 1: "))
br2 = int(input("Unesi broj za 2: "))
br3 = int(input("Unesi broj za 3: "))
br4 = int(input("Unesi broj za 4: "))

print("Najveći broj je: {}".format(funkc(br1,br2,br3,br4)))