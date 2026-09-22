#This is a password Generator

import random

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
         '-', '_', '+', '=', '?', '/', '<', '>', '.']

print("\n\n\n-----------------------------------------------------------------------------------------------------------------------")
print("SHORT PASSWORDS ARE EASIER TO GUESS OR CRACK, WHILE LONGER PASSWORDS ARE HARDER TO BREAK. A STRONG PASSWORD SHOULD BE LONG, UNIQUE, AND CONTAIN A MIX OF LETTERS, NUMBERS, AND SPECIAL CHARACTERS. THIS PASSWORD GENERATOR HELPS YOU CREATE STRONG AND SECURE PASSWORDS EASILY.")
print("-----------------------------------------------------------------------------------------------------------------------")

print("\n\n\n-------------------Password Generator--------------------")
nl=int(input("\nEnter the number of letters you wantin your password: "))
nd=int(input("\nEnter the number of digits you wantin your password: "))
ns=int(input("\nEnter the number of symbols you wantin your password: "))

pl=[]

for i in range(0,nl):
    pl.append(random.choice(letters))

for i in range(0,nd):
    pl.append(random.choice(digits))

for i in range(0,ns):
    pl.append(random.choice(symbols))

random.shuffle(pl)
finalpassword=''.join(pl)

print("\n\n\nGENERATED PASSWORD:  ",finalpassword,"\n\n\n")



