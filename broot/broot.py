import random
import os
import re
import string

os.system("cls")

symbols = ".!?#-"

def ParseFile(fil):
    with open(fil, 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))
    out = [line for line in unique_lines if not re.fullmatch(r'\d+', line.strip())]

    with open(fil, 'w') as file:
        file.writelines(out)

def BrootMain(testmode=False):
    Extratags = input("Add known things (must be 3 or more things): ").split(',')

    Amount = input("How many passwords to generate (not accurate! may generate more or less):  ")

    if not Extratags:
        print(" Please fill in the required fields! (Error Code: 150)")
        return 150

    passwords = []
    passwords_2 = []
    passwords_3 = []
    
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

    print("Done! Don't exit, we're storing the passwords to ./passwords-broot.txt")

    with open("./passwords-broot.txt", 'a') as f:
        for pwd in passwords:
            f.write(pwd + "\n")
        for pwd2 in passwords_2:
            f.write(pwd2 + "\n")
        for pwd3 in passwords_3:
            f.write(pwd3 + "\n")
    
    ParseFile("./passwords-broot.txt")

while True:
    try:
        BrootMain(testmode=True)
        os.system("cls")
    except KeyboardInterrupt:
        print("Leaving.. bye!")
        quit()
