r = int(input("Enter Rook's row position: "))
c = int(input("Enter Rook's column position: "))

ROW = 8
COL = 8


def rook(pos):
    x, y = pos
    res = []
    for i in range(ROW):
        row = []
        for j in range(COL):
            if j == y or i == x:
                row.append(1)
            else:
                row.append(0)
        res.append(row)
    res[x][y] = 5
    return res


b = rook((r, c))

for row in b:
    print("-----------------")
    for col in row:
        print("|", end="")
        if col == 1:
            print("x", end="")
        elif col == 5:
            print("R", end="")
        else:
            print(" ", end="")
    print("|")
print("-----------------")
