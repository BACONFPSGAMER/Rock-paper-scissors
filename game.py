from random import randint
import time

t = ["Rock","Paper","Scissors"]

c = t[randint(0,2)]

player = False

while player == False:
    player = input("Enter your choice(Rock,Paper,Scissors or q?")

    if player == c:
        print("computer choses",c)
        print("player chooses",player)
        time.sleep(2)
        print("Its a Tie!")

    elif player == "Rock":
        if c == "Paper":
            print("Player Chooses",player)
            print("Computer chooses",c)
            time.sleep(2)
            print("You lost...",c,"covers",player)
        else:
            print("player chooses",player)
            print("Computer chooses",c)
            time.sleep(2)
            print("You lost...",c,"covers",player)

    elif player == "Paper":
        if c == "Scissors":
            print("Player Chooses",player)
            print("Computer chooses",c)
            time.sleep(2)
            print("You lost...",c,"Cut",player)
        else:
            print("player chooses",player)
            print("Computer chooses",c)
            time.sleep(2)
            print("You lost...",player,"Cuts",c)


    elif player == "Scissors":
        if c == "Rock":
            print("Player Chooses",player)
            print("Computer chooses",c)
            time.sleep(2)
            print("You lost...",c,"smashes",player)
        else:
            print("player chooses",player)
            print("Computer chooses",c)
            time.sleep(2)
            print("You lost...",c,"cut",player)

    elif player == "q":
        print("hoped u enjoyed the game.")
        break

    else:
        print("TNAVI ERROR. please try again")

    player = False
    c = t[randint(0,2)]
    
