from random import choice, random
sten = 1
sax = 2
påse = 3
points = 0
aipoints = 0
gamer = ""
dator = ""
import random

print("Välkommen till sten, sax eller påse.")
svar = input("[1] Spela\n[2] Exit\n")
while svar == "1":
    gamer = input ("Välj mellan\n[1]Sten\n[2]Sax\n[3]Påse\n")
    dator = str(random.randint (1,3))
    if gamer == dator:
        print(f"Lika! Du har fortfarande {points} poäng och datorn {aipoints} poäng.")
    elif gamer == "1":
        if dator == "2":
            points += 1
            print(f"Du fick ett poäng! Du har {points} poäng.")
            print(f"Datorn har fortfarande {aipoints} poäng.")
        elif dator == "3":
            aipoints += 1
            print(f"Du är sämst, du har fortfarande {points} poäng.")
            print(f"Ser du vad du har gjort? Datorn har nu {aipoints} poäng.")
    elif gamer == "2":
        if dator == "3":
            points += 1
            print(f"Du fick ett poäng! Du har {points} poäng.")
            print(f"Datorn har fortfarande {aipoints} poäng.")
        elif dator == "1":
            aipoints += 1
            print(f"Du är sämst, du har fortfarande {points} poäng.")
            print(f"Ser du vad du har gjort? Datorn har nu {aipoints} poäng.")
    elif gamer == "3":
        if dator == "1":
            points += 1
            print(f"Du fick ett poäng! Du har {points} poäng.")
            print(f"Datorn har fortfarande {aipoints} poäng.")
        elif dator == "2":
            aipoints += 1
            print(f"Du är sämst, du har fortfarande {points} poäng.")
            print(f"Ser du vad du har gjort? Datorn har nu {aipoints} poäng.")
    if points == 2:
        print("Du vann över dator jäveln 👍")
        svar = input("Vad vill du göra?\n[1] Spela igen?\n[2] Exit?\n")
        points = 0
        aipoints = 0

    if aipoints == 2:
        print("Du suger din skitunge, datorn vann.")
        svar = input("Vad vill du göra nu?\n[1] Spela igen?\n[2] Exit?\n")
        points = 0
        aipoints = 0