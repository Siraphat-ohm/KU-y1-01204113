def readInput():
    numbers = []
    while True:
        n = input("Enter score (or just ENTER to finish): ")
        if n == "":
            break
        numbers.append(int(n))
    return numbers


def grade(s, u, sd):

    if s >= u + 1.5 * sd:
        return "A"
    elif s >= u + 1.0 * sd and s < u + 1.5 * sd:
        return "B+"
    elif s >= u + 0.5 * sd and s < u + 1.0 * sd:
        return "B"
    elif s >= u and s < u + 0.5 * sd:
        return "C+"
    elif s >= u - 0.5 * sd and s < u:
        return "C"
    elif s >= u - 1.0 * sd and s < u - 0.5 * sd:
        return "D+"
    elif s >= u - 1.5 * sd and s < u - 1.0 * sd:
        return "D"
    elif s < u - 1.5 * sd:
        return "F"


def main():
    numbers = readInput()
    length = len(numbers)
    avg = sum(numbers) / length
    sd = 0

    for n in numbers:
        sd += (n - avg) ** 2
    sd = (sd / (length - 1)) ** 0.5
    print(f"Average score is {avg:.2f}")
    print(f"Standard deviation is {sd:.2f}")
    for i, n in enumerate(numbers):
        g = grade(n, avg, sd)
        print(f"Score #{i+1}: {n} grade: {g}")


main()
