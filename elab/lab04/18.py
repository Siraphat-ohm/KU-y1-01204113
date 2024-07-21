number = 21


def count_digits(number):
    n = str(number)
    i = 0
    count = 0

    while i < len(n):
        if n[i].isdigit():
            count += 1
        i += 1
    return count


print(f"There are {count_digits(number)} digits in {number}")
