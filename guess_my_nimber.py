import random
print ("\tChislo ot 1 lj 100")
the_number = random.randint(1, 100)
guess = int(input("Vashe chisko: "))
tries = 1
while guess != the_number:
    if tries > 10:
        print("Vse ochen ploho")
        print("chislo", the_number)
        break
    if guess > the_number:
        print("Menshe")
    else:
        print("Bolshe")
    guess = int(input("Vashe chislo: "))
    tries += 1
    if guess == the_number:
        print("Vse poluchilos", the_number)
        print("Popitok", tries)
        break
