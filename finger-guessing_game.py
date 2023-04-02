from random import randint
hands = ("Rock","Scissors","Paper")
s_hand = input("input(O:Rock,1:Scissors,2:Paper):")
if s_hand not in ['0', '1', '2']:
    print("not proper choice!exit!")
    exit()
choice = int(s_hand)
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
    elif choice == 1:
        if computer == 0:
            print("you lose")
        else:
            print("you win")
    else:
        if computer == 0:
            print("you win")
        elif computer == 1:
            print("you lose")
