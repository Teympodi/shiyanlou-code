from random import randint
hands = ("Rock","Scissors","Paper")
choice = int(input("input(0:Rock,1:Scissors,2:paper):"))
computer = randint(0,2)
print("you:",hands[choice]," ; computer:",hands[computer])
if choice == computer:
    print("draw!")
else:
    if choice == 0:
        if computer == 1:
            print("you win")
        else:
            print("you lose")
    elif choile == 1:
        if computer == 0:
            print("you lose")
        else:
            print("you win")
    else:
        if computer == 0:
            print("you win")
        else:
            print("you lose")
