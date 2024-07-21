def readInput():
    d = int(input("How deep is the well? "))
    h = int(input("How high the frog can jump up? "))
    f = int(input("How far the frog slips down? "))
    return (d, h, f)


def main():
    d, h, f = readInput()
    if f > h or (d > h and d > f and f == h):
        print("The frog is always stuck in the well.")
        return
    days = 0
    while d > 0:
        days += 1
        d -= h
        if d <= 0:
            break
        print(f"On day {days} the frog leaps to the depth of {d} meters.")
        d += f
        print(f"At night he slips down to the depth of {d} meters.")
    print(f"The frog gets out of the well on day {days}.")


main()
