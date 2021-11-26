#   Napišite program koji od korisnika učitava stringove i odmah ih ispisuje.
#   Neka korisnik unosi stringove dok god to želi (nakon svakog stringa ga pitajte želi li unijeti još jedan).
#   Na kraju ispišite ukupan broj znakova u svim stringovima koje je korisnik unio

arr_str = []


def brojac(arra):
    for i in range (len(arra)):
        print("String broj {} ima {} znakova.".format(i, len(arra[i])))


while True:
    str = input("unesi zeljeni string: ")
    arr_str.append(str)
    chc = input("Jos jedan? (d/n)")
    print (arr_str)
    if chc == "d":
        continue
    elif chc == "n":
        break

print(arr_str) 
print(brojac(arr_str))        
        
    

