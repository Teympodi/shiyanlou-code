#!/usr/bin/python3
a = input("How many apples do you have:")
print("You have got " + a + " apples!")
b = input("How many banana do you have:")
print("You have got " + b + " bananas!")
try:
    total = int(a) + int(b)
    print("You have got " + str(total) + " fruits in all!")
except:
    print("\033[41m[error]\033[0m -----Input numbers!!!")
