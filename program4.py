import random

def roll(num):
    return random.randint(1, num)

num = int(input("How many faces would you like your die to have? "))
res = 0

while res != num:
    res = roll(num)
    print("You rolled a", res)
