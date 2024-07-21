def readInput():
    s = int(input("Input starting food (S): "))
    p = int(input("Input Paun's eating rate (P): "))
    g = int(input("Input Gane's eating rate (G): "))
    return (s, p, g)


def eat(S, P, G):
    p = S // P
    g = (S - (P * p)) // G
    d = S - p * P - g * G

    return (p, g, d)


# s, p, g = readInput()
# s = (197, 70, 11)

p, g, d = eat(*readInput())

print(f"Paun eats {p} time(s)")
print(f"Gane eats {g} time(s)")
print(f"Remaining {d} for dog")
