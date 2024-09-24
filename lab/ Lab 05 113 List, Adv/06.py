numbers = list(map(int, input().split()))
while True:
    menu, x = input().split()
    x = int(x)

    if menu == "E":
        break
    elif menu == "A":
        numbers.append(x)
    elif menu == "S":
        print(numbers[x])
    elif menu == "R":
        del numbers[x]

print(" ".join([str(i) for i in numbers]))
