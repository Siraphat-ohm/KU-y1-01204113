n = 100


def isPrime(num):
    flag = 1
    for i in range(2, num // 2 + 1):
        if (num % i) == 0:
            flag = 0
            break

    return flag == 1


def printAllPrimes(limit):
    l = []
    for i in range(2, limit + 1):
        if isPrime(i):
            l.append(str(i))
    print(" ".join(l))


printAllPrimes(10)
