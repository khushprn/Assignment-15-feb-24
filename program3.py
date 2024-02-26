import random

def roll():
    return random.randint(1, 6)

res = 0
while res != 6:
    res = roll()
    print("You rolled a", res)
