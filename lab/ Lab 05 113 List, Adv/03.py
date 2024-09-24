# levels = 2
# size = 3  # size * 2 - 1

levels = int(input("Enter number of levels: "))
size = int(input("Enter size of each bush: "))

for _ in range(levels):
    for i in range(size, 0, -1):
        print(" " * (i - 1) + "*" * (2 * (size - i) + 1))
