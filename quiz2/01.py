rat = '__QQ\n()">'.split("\n")
hunter = " O \n/|\\\n/ \\".split("\n")
lion = " /\_/\ \n( o.o )\n > ^ < ".split("\n")

choices = {1: rat, 2: hunter, 3: lion}

n1 = input("Player1 name: ")
n2 = input("Player2 name: ")

s1 = 0
s2 = 0


def draw(c1, c2):
    l_c1, l_c2 = len(c1), len(c2)
    line = max(l_c1, l_c2)
    for i in range(line):
        if i < l_c1:
            print(c1[i], end="  ")
        else:
            print("    ", end="  ")

        if i == line // 2:
            print("VS", end="  ")
        else:
            print("  ", end="  ")

        if i < l_c2:
            print(c2[i], end="  ")
        else:
            print("    ", end="  ")

        print()


def showscore():
    print(f"{n1} {s1} / {n2} {s2}")


def readc():
    p1c = int(input(f"{n1}'s choice (1/rat, 2/hunter and 3/lion): "))

    p2c = int(input(f"{n2}'s choice (1/rat, 2/hunter and 3/lion): "))

    return (p1c, p2c)


for i in range(5):
    print()
    print(f"Round {i+1}!")
    showscore()
    c1, c2 = readc()
    if c1 == 3 and c2 == 1:
        s1 += 1
    if c1 == 3 and c2 == 2:
        s2 += 1

    if c1 == 2 and c2 == 1:
        s2 += 1
    if c1 == 2 and c2 == 3:
        s1 += 1

    if c1 == 1 and c2 == 2:
        s1 += 1
    if c1 == 1 and c2 == 3:
        s2 += 1
    draw(choices[c1], choices[c2])
    if s1 == 3 or s2 == 3:
        print()
        showscore()
        if s1 > s2:
            print(f"{n1} win!")
        else:
            print(f"{n2} win!")
        break

if s1 == s2:
    print()
    showscore()
    print("Draw!")
print()
