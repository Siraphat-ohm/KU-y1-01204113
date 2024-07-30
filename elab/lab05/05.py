def readInput():
    d = input("d: ")
    m = input("m: ")
    y = int(input("y: "))
    # d = "31"
    # m = "12"
    # y = 1994

    if d[0] == "0":
        d = int(d[1])
    else:
        d = int(d)
    if m[0] == "0":
        m = int(m[1])
    else:
        m = int(m)
    return (d, m, y)


def isLeap(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False


def mtoday(m, y):
    if m == 1:
        return 31
    elif m == 2:
        return 29 if isLeap(y) else 28
    elif m == 3:
        return 31
    elif m == 4:
        return 30
    elif m == 5:
        return 31
    elif m == 6:
        return 30
    elif m == 7:
        return 31
    elif m == 8:
        return 31
    elif m == 9:
        return 30
    elif m == 10:
        return 31
    elif m == 11:
        return 30
    else:
        return 31


d, m, y = readInput()
dofy = 0

for i in range(m - 1):
    dofy += mtoday(i + 1, y)
print(dofy + d)
