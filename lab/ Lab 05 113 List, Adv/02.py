def list_factors(n):
    factors = ""
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors += f"{i} "
    factors += f"{n} "
    return factors


def find_sum_and_num_factors(n):
    factors = [int(i) for i in list_factors(n).split()]
    s = sum(factors)
    return (s, len(factors))


def isPrime(num):
    flag = 1
    for i in range(2, num // 2 + 1):
        if (num % i) == 0:
            flag = 0
            break

    return flag == 1


n = int(input("Enter positive number: "))
facs = list_factors(n)
print(f"Factors of {n} are")
print(facs)
s, c = find_sum_and_num_factors(n)
print(f"Sum of {facs}is {s}")
print(f"Number of factors is {c}")
print(f"{n} is prime number." if isPrime(n) and n != 1 else f"{n} is not prime number.")
