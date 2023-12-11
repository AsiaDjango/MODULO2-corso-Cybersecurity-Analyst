import random

corta = 8
lunga = 20

def genera_pwd_debole(crea):
   lettere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

   pwd_debole = ''.join(random.choice(lettere) for debole in range (corta))
   return pwd_debole

def genera_pwd_forte(crea):
   lettere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
   numeri = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
   simboli = ["!", "?", "$", "£", "%", "&", "=", "*", "#", "+", "§"]

   frulla_tutto = lettere+numeri+simboli

   pwd_forte = ''.join(random.choice(frulla_tutto) for forte in range (lunga))
   return pwd_forte

crea = input("""Di che tipo di password hai bisogno?
A) la mia vita è complicata, quindi voglio una password semplice
B) la mia vita è semplice, quindi voglio una password complicata
C) non mi interessa \n""").lower()

if (crea == 'a'):
    print ('\nEcco la tua password: ')
    print (genera_pwd_debole(crea))

elif (crea == 'b'):
    print ('\nEcco la tua password: ')
    print (genera_pwd_forte(crea))

elif (crea == 'c'):
    print ('\nPazienza, buona continuazione!')

else:
    print ('\nQualcosa non va... riprova')
