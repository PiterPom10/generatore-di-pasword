
import random
elementi = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lunghezza = int(input("inserire la lunghezza"))

password_autogenerata = ("")        

for i in range(lunghezza):
    carattere_casuale = random.choice(elementi)
    password_autogenerata = carattere_casuale

    print(password_autogenerata)

