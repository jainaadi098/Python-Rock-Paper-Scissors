import random

choices=["ROCK","PAPER","SCISSOR","EXIT"]

def valid_input():
    while True:
        choice=input("Enter Your Choice :")
        choice=choice.upper().strip()
        if choice in choices:
            return choice
        else:
            print("Invalid Input")

print("ROCK PAPER SCISSOR GAME")

while True:
    Player_choice=valid_input()
    
    if Player_choice=="EXIT":
        print("You Quit")
        break
    
    Computer_choice=random.choice(["ROCK","PAPER","SCISSOR"])
    print("Computer Choice : ",Computer_choice)
    
    


    if Player_choice==Computer_choice:
        print("DRAW")
    elif Player_choice=="ROCK" and Computer_choice=="PAPER":
        print("COMPUTER WINS")
    elif Player_choice=="ROCK" and Computer_choice=="SCISSOR":
        print("PLAYER WINS")
    elif Player_choice=="PAPER" and Computer_choice=="ROCK":
        print("PLAYER WINS")
    elif Player_choice=="PAPER" and Computer_choice=="SCISSOR":
        print("COMPUTER WINS")
    elif Player_choice=="SCISSOR" and Computer_choice=="ROCK":
        print("COMPUTER WINS")
    elif Player_choice=="SCISSOR" and Computer_choice=="PAPER":
        print("PLAYER WINS")
    else:
        print("INVALID INPUT")
