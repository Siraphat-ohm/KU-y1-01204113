n = int(input("Day: "))
f = 0
p, f = 0, 1
print(f, end=" ")
for _ in range(2, n + 1):
    p, f = f, f + p
    print(f, end=" ")
