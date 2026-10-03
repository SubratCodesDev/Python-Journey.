print('''!WELCOME TO GAMEZONE!          
      ===~SNAKE, WATER AND GUN GAME~===
           1.SNAKE WINS OVER WATER
           2.WATER WINS OVER GUN
           3.GUN WINS OVER SNAKE''')
import random
while True:
    computer = random.choice(["SNAKE", "WATER", "GUN"])
    nn=input("Enter your choice:")
    print("Computer chose",computer)
    if computer==nn:
        print("OPOOS DRAW.TRY AGAIN")
    elif computer=="SNAKE" and nn=="WATER":
        print("You loose")
    elif computer=="SNAKE" and nn=="GUN":
        print("You win")
    elif computer=="WATER" and nn=="GUN":
        print("You loose")
    elif computer=="WATER" and nn=="SNAKE":
        print("You win")
    elif computer=="GUN" and nn=="WATER":
        print("You win")
    elif computer=="GUN" and nn=="SNAKE":
        print("You loose")
    else:
        print("Something went wrong,Try again")
    again = input("Do you want to play again? (yes/no): ").lower()

    if again == "no":
        print("Thanks for playing!")
        break