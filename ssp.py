import random
points = 0
aipoints = 0
player = ""
ai = ""

print("Välkommen till sten, sax eller påse.")
choice = input("[1] Spela\n[2] Exit\n")
while choice == "1":
    player = input ("Välj mellan\n[1]Sten\n[2]Sax\n[3]Påse\n")
    ai = str(random.randint (1,3))
    if player == ai:
        print(f"Lika! Du har fortfarande {points} poäng och AI {aipoints} poäng.")
    elif player == "1":
        if ai == "2":
            points += 1
            print(f"Du fick ett poäng! Du har {points} poäng.")
            print(f"AI har fortfarande {aipoints} poäng.")
        elif ai == "3":
            aipoints += 1
            print(f"Du är sämst, du har fortfarande {points} poäng.")
            print(f"Ser du vad du har gjort? AI har nu {aipoints} poäng.")
    elif player == "2":
        if ai == "3":
            points += 1
            print(f"Du fick ett poäng! Du har {points} poäng.")
            print(f"AI har fortfarande {aipoints} poäng.")
        elif ai == "1":
            aipoints += 1
            print(f"Du är sämst, du har fortfarande {points} poäng.")
            print(f"Ser du vad du har gjort? AI har nu {aipoints} poäng.")
    elif player == "3":
        if ai == "1":
            points += 1
            print(f"Du fick ett poäng! Du har {points} poäng.")
            print(f"AI har fortfarande {aipoints} poäng.")
        elif ai == "2":
            aipoints += 1
            print(f"Du är sämst, du har fortfarande {points} poäng.")
            print(f"Ser du vad du har gjort? AI har nu {aipoints} poäng.")
    if points == 2:
        print("Du vann över AI jäveln 👍")
        choice = input("Vad vill du göra?\n[1] Spela igen?\n[2] Exit?\n")
        points = 0
        aipoints = 0

    if aipoints == 2:
        print("Du suger din skitunge, du lät AI vinna.")
        choice = input("Vad vill du göra nu?\n[1] Spela igen?\n[2] Exit?\n")
        points = 0
        aipoints = 0