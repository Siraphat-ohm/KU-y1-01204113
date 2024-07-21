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
    for i, n in enumerate(numbers):
        print(f"Score #{i+1}: {n}")

    Max, Min = max(numbers), min(numbers)
    avg = sum(numbers) / len(numbers)

    print(f"Average score is {avg:.2f}")
    print(f"Minimum score is {Min}")
    print(f"Maximum score is {Max}")


main()
