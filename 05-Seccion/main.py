#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]  #52
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letras_total = ("")
for letras in range(0, nr_letters):
    letra_azar = random.randint(0, 51)
    letra_azar1 = letters[letra_azar]
    letras_total += str(letra_azar1)

symb_total = ("")
for simb in range(0, nr_symbols):
    symb_azar = random.randint(0, simb)
    symb_azar1 = symbols[symb_azar]
    symb_total += str(symb_azar1)

numb_total = ("")
for numb in range(0, nr_numbers):
    numb_azar = random.randint(0, numb)
    numb_azar1 = numbers[numb_azar]
    numb_total += numb_azar1

password = list(letras_total + symb_total + numb_total)

pw_end = ("")
for pw in range(0, len(password)):
    pw_azar = random.randint(0, len(password) - 1)
    pw_azar1 = password[pw_azar]
    pw_end += str(pw_azar1)
    password.remove(password[pw_azar])
print(f"\nYour New Password is: {pw_end}")