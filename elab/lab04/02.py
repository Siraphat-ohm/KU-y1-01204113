def readInput():
    numbers = []
    while True:
        n = float(input("Enter a number (or just zero to exit): "))
        if not n:
            break
        numbers.append(n)
    return numbers


numbers = readInput()
p_s = 0
n_s = 0
for n in numbers:
    if n < 0:
        n_s += n
    else:
        p_s += n

print(f"Sum of all positive numbers is {p_s:.2f}")
print(f"Sum of all negative numbers is {n_s:.2f}")
