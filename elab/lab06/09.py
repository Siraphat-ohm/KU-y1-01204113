num = int(input("Enter the number of rows or columns : "))


for i in range(num):
    for j in range(i + 1, i + num + 1):
        print(f"%2d" % j, end=" ")
    print()
