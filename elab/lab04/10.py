d = int(input("Distance from starting point(m.): "))
# f -> 5 , b -> 2
# b <- 4 , b -> 3
m = 0
sets = 0
while m < d:
    m += 5
    print(m, end=" ")
    m -= 2
    print(m, end=" ")
    sets += 1

while m > d:
    m -= 4
    print(m, end=" ")
    m += 3
    print(m, end=" ")
    sets += 1

if d == 0:
    print(0, end="")
print()
print(f"Buzz moved {sets} set(s)")
