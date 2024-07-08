import random
import os
import re
import string

def ParseFile(fil):
    with open(fil, 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))
    out = [line for line in unique_lines if not re.fullmatch(r'\d+', line.strip())]

    with open(fil, 'w') as file:
        file.writelines(out)

while True:
    symbols = ".!?#-"

    Extratags = input("Add stuff (Seperate by comma): ").split(',')
    Amount = input("Enter the amount of passwords: ")

    passwords = []

    passwords_2 = [] # All lowercase
    passwords_3 = [] # All upercase
    passwords_4 = [] # No symbols
    passwords_5 = [] # No numbers

    components = Extratags

    for tag in Extratags:
        passwords.append(tag)

    for _ in range(int(Amount)):
        password = ""
        num_parts = random.randint(1, 3)

        parts = random.sample(components, num_parts)

        for p in parts:
            password += p

        if random.choice([True, False]):
            password += str(random.randint(0, 1000))
        
        if random.choice([True, False]):
            if random.choice([True, False]):
                password = random.choice(symbols) + password
            else:
                password += random.choice(symbols)

        if password:
            index = random.randint(0, len(password) - 1)
            if password[index].isalpha():
                password = password[:index] + password[index].upper() + password[index+1:]

        passwords.append(password)

    passwords_2 = [element.lower() for element in passwords]
    passwords_3 = [element.upper() for element in passwords]

    passwords_4 = [''.join(re.findall(r'\w', element)) for element in passwords]
    passwords_5 = [''.join(re.findall(r'[A-Za-z]', element)).upper() for element in passwords]


    print("Don't exit, we're storing the passwords to ./passwords.txt")

    with open("./passwords.txt", 'a') as f:
        for pwd in passwords: f.write(pwd + "\n")
        for pwd2 in passwords_2: f.write(pwd2 + "\n")
        for pwd3 in passwords_3: f.write(pwd3 + "\n")
        for pwd4 in passwords_4: f.write(pwd4 + "\n")
        for pwd5 in passwords_5: f.write(pwd5 + "\n")

    ParseFile("./passwords.txt")