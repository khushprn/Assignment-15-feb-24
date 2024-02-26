import random

n = int(input("How many dice do you want to roll? "))
s = 0

for i in range(n):
    r = random.randint(1, 6)
    s += r

print("The sum of the numbers rolled is:",s)