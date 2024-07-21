def count_digits(number):
    n = str(number)
    i = 0
    count = 0

    while i < len(n):
        if n[i].isdigit():
            count += 1
        i += 1
    return count


def get_last_digit(n):
    return n % 10


def get_distribution(number):
    string = ""
    n = count_digits(number)
    for i in range(n):
        last = get_last_digit(number // 10**i)
        if i == n - 1:
            string += f"{last}x10^{i}"
        else:
            string += f"{last}x10^{i} + "
    return string


number = int(input("Input number: "))
print(f"{number} = {get_distribution(number)}")
