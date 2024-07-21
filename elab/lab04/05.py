def readInput():
    numbers = []
    while True:
        n = input("Enter score (or just ENTER to finish): ")
        if n == "":
            break
        numbers.append(int(n))
    return numbers


def main():
    numbers = readInput()
    numbers = sorted(numbers)[::-1]
    for i, n in enumerate(numbers):
        print(f"Rank #{i+1}: {n}")


main()
