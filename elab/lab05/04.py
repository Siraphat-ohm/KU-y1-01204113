# n = 7
n = int(input("input: "))

u = n // 2
for i in range(u, -1, -1):
    print(" " * i + "#" * (2 * (u - i) + 1))

for i in range(1, u + 1):
    print(" " * i + "#" * (2 * (u - i) + 1))
