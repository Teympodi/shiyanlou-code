from random import randint
key = randint(1,100)
choice = 0
while True:
    choice = input("Your choice:")
    try:
        choice = int(choice)
    except ValueError:
        print("\33[41merror\33[0mnot valid number")
    else:
        if choice < 0:
            print("\33[41merror\33[0m less than 0")
        elif choice > 100:
            print("\33[41merror\33[0m more than 100")
        elif choice ==key:
            break
        elif key > choice:
            print("go higher")
        else:
            print("go lower")
print("you got the right number",choice)
