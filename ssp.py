from random import random
sten = 1
sax = 2
påse = 3
gamer = ""
dator = ""
import random

print("Välkommen till sten, sax eller påse.")
svar = input("[1] Spela\n[2] Exit\n")
while svar == "1":
    gamer = input ("Välj mellan\n[1]Sten\n[2]Sax\n[3]Påse\n")
    dator = str(random.randint (1,3))
    