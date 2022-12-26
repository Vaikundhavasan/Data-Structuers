import random

print("Implement Application using Lists")
print("..................................")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
           "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many Numbers would you like in your password?\n"))
nr_symbols = int(input("How man  Symbols would you like in your password?\n"))

letter = ""
for i in range(1,nr_letters+1):
    total_letter=random.choice(letters)
    letter += total_letter

number = ""
for i in range(1,nr_numbers+1):
    total_numbers=random.choice(numbers)
    number += total_numbers

symbol = ""
for i in range(1,nr_symbols+1):
    total_symbols=random.choice(symbols)
    symbol += total_symbols

password=letter+number+symbol
print(password)
