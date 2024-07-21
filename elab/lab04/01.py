def readInput():
    numbers = []
    while True:
        n = input("Enter a number (or [Enter] to stop): ")
        if n == "":
            break
        numbers.append(float(n))
    return numbers


numbers = readInput()
n = len(numbers)
if not n:
    print("Nothing to do.")
else:
    avg = sum(numbers) / n

    print(f"The maximum value is {max(numbers):.2f}")
    print(f"The minimum value is {min(numbers):.2f}")
    print(f"The average value is {avg:.2f}")
