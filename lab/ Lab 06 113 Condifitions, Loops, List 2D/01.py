def box(n):
    print("." * n)
    k = n // 2
    i = 0
    for i in range(k - 1):
        print("." + " " * i + "." + " " * (2 * (k - i - 1) - 1) + "." + " " * i + ".")
    print("." + " " * (i + 1) + "." + " " * (i + 1) + ".")
    for j in range(k - 1, 0, -1):
        print(
            "."
            + " " * (j - 1)
            + "."
            + " " * (2 * (k - j) - 1)
            + "."
            + " " * (j - 1)
            + "."
        )
    print("." * n)


n = int(input())


if n >= 9 and n % 2 != 0:
    box(n)
