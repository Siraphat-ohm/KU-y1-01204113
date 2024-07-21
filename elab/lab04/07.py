string = input("Enter a string: ")
n = len(string)

for i in range(n):
    for j in range(i):
        print(" ", end="")
    print(string[i])
