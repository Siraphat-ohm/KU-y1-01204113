def DrawRat():
    s = '__QQ\n()">\n'
    print(s)


def DrawHunter():
    s = " O\n/|\ \n/ \ \n"
    print(s)


def DrawLion():
    s = " /\_/\ \n( o.o )\n > ^ <\n"
    print(s)


def cal(c1, c2, p1, p2):
    diff = abs(c2 - c1)
    if diff >= 0 and diff <= 1:
        if c1 < c2:
            p1["score"] += 1
        elif c1 > c2:
            p2["score"] += 1
    else:
        if c1 > c2:
            p1["score"] += 1
        elif c1 < c2:
            p2["score"] += 1


def showScore():
    print(p1["n"], p1["score"], "/", end=" ")
    print(p2["n"], p2["score"])


def readC():
    p1c = int(input(f"{p1['n']}'s choice (1/rat, 2/hunter and 3/lion): "))

    p2c = int(input(f"{p2['n']}'s choice (1/rat, 2/hunter and 3/lion): "))
    return (p1c, p2c)


def whoWin(r):
    s1, s2 = p1["score"], p2["score"]
    if r == 2:
        if s1 - s2 >= 2:
            showScore()
            print(f"{n1} win!")
            return 1
        elif s2 - s1 >= 2:
            showScore()
            print(f"{n2} win!")
            return 1
    elif r == 3:
        if s1 > s2:
            showScore()
            print(f"{n1} win!")
        elif s2 > s1:
            showScore()
            print(f"{n2} win!")
        elif s1 == s2:
            showScore()
            print("Draw!")


def game(r, p1, p2):
    print()
    n1, n2 = p1["n"], p2["n"]
    print(f"Round {r}!")
    showScore()
    c1, c2 = readC()

    print(n1)
    choices[c1]()

    print("VS")

    print(n2)
    choices[c2]()

    cal(c1, c2, p1, p2)


choices = {1: DrawRat, 2: DrawHunter, 3: DrawLion}

n1 = input("Player1 name: ")
n2 = input("Player2 name: ")

p1 = {"n": n1, "score": 0}
p2 = {"n": n2, "score": 0}


def main():

    game(1, p1, p2)
    game(2, p1, p2)
    if whoWin(2):
        return
    game(3, p1, p2)
    whoWin(3)


main()
