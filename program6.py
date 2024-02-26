def rem(n):
    even = []
    for num in n:
        if num % 2 == 0:
            even.append(num)
    return even

numbr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut = rem(numbr)

print("Original list:", numbr)
print("Cut-down list (without odd numbers):", cut)
