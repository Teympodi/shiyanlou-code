import random
cards = []
for n in range(0x1f0a0,0x1f0e0):
    if n % 16 == 0 or n % 16 == 12:
        continue
    cards.append(chr(n))
cards.remove(chr(0x1f0bf))
cards.remove(chr(0x1f0af))
random.shuffle(cards)
print(cards)
dong = cards[0:48:4]
dong.sort()
nan = cards[1:48:4]
nan.sort()
xi = cards[2:48:4]
xi.sort()
bei = cards[3:48:4]
bei.sort()
di = cards[-6:]
print("东:",dong)
print(len(dong))
print("南:",nan)
print(len(nan))
print("西:",xi)
print(len(xi))
print("北:",bei)
print(len(bei))
print("底:",di)
print(len(di))
print(len(dong) + len(nan) + len(xi) + len(bei) + len(di))
