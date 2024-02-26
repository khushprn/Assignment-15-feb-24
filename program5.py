def con(gall):
    lit = gall * 3.78541
    return lit


while True:
    g = float(input("How many gallons of gasoline do you have? (Enter a negative value to exit): "))

    if g < 0:
        print("Exit the program")
        break

    litr = con(g)
    print("You have", litr, "liters of gasoline.")
