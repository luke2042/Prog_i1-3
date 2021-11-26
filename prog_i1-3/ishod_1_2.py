#•	Napišite program koji od korisnika učitava neparni broj n (ako korisnik unese parni broj, samo završite program)
#  i iscrtava romb čije obje dijagonale imaju po n znakova. Primjerice, ako je n = 7:
   #
  ###
 #####
#######
 #####
  ###
   #

def provjera(x):
    #Paran = false
    z = x%2
    if z != 0:
        return False
    else:
        return True
flag = False

n = int(input("Unesite neparni broj: "))
provjera(n)
if provjera == False:
    exit

spc = " "
toc = "#"
brojspc = int(n/2)
brojtpc = 1
for z in range(n):

    for i in range(brojspc):
        print(spc, end = '')

    for x in range(brojtpc):
        print(toc, end = '')
    
    redak = z
    if redak <n/2-1:
        brojspc -=1
        brojtpc +=2
    else:
        brojspc +=1
        brojtpc -=2

    print("\n")
    

