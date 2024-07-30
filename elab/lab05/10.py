numbers = list(map(int, input().split()))
# numbers = [1, 2, 3, 4, 5]
# numbers = [-10, -9, -8, -7, 34]

length = len(numbers)

while True:
    x, y = list(map(int, input().split()))
    if x < 0:
        x += length

    if y < 0:
        y += length

    if x >= 0 and x < length and y >= 0 and y < length:
        if x > y:
            break
        print(sum(numbers[x : y + 1]))
    else:
        x_con = x < 0 or x >= length
        y_con = y < 0 or y >= length

        if x_con and y_con:
            print("x and y Bad Input")
        elif x_con:
            print("x Bad Input")
        elif y_con:
            print("y Bad Input")
