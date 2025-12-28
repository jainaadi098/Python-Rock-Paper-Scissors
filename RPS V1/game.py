import random

print("ROCK PAPER SCISSORS GAME")
Player_choice=input("Enter Your Choice :")
Player_choice=Player_choice.upper().strip()


Computer_choice=random.choice(["ROCK","PAPER","SCISSORS"])
print("Computer Choice : ",Computer_choice)

if Player_choice==Computer_choice:
    print("DRAW")
elif Player_choice=="ROCK" and Computer_choice=="PAPER":
    print("COMPUTER WINS")
elif Player_choice=="ROCK" and Computer_choice=="SCISSORS":
    print("PLAYER WINS")
elif Player_choice=="PAPER" and Computer_choice=="ROCK":
    print("PLAYER WINS")
elif Player_choice=="PAPER" and Computer_choice=="SCISSORS":
    print("COMPUTER WINS")
elif Player_choice=="SCISSORS" and Computer_choice=="ROCK":
    print("COMPUTER WINS")
elif Player_choice=="SCISSORS" and Computer_choice=="PAPER":
    print("PLAYER WINS")
else:
    print("INVALID INPUT")
