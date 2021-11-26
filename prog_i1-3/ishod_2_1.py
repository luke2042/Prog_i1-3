#	Napišite program koji u listu učitava 5 cijelih brojeva od korisnika.
#   Napravite novu listu i u nju prepišite sadržaj prve liste, ali obrnutim redoslijedom.
#   Primjerice, ako je prva lista [7, 1, 3, 8, 5], onda druga lista mora biti [5, 8, 3, 1, 7].

list = []
print("Unesi 5 cijelih brojeva: ")

for i in range(5):
    x = int(input())
    list.append(x)

list2 = []
print()
for x in range(1, 6):
    list2.append(list[-x])

print(list, list2)