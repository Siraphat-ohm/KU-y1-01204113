n = 15


def AlterSum(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += -i
        else:
            s += i
    return s
