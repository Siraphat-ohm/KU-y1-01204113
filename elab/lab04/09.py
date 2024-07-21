def readInput():
    return [int(n) for n in input().split(" ")]


def plus(t, v):
    return t + v


def minus(t, v):
    return t - v


n = int(input("How many food you have : "))

s = 0
for i in range(n):
    t, v = readInput()
    if v < 0 or t < 0:
        s += -minus(0, t * v)
    else:
        s += plus(0, t * v)


print(s)
