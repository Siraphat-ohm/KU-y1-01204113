import random

rat = '__QQ\n()">'
hunter = " O \n/|\\\n/ \\"
lion = " /\\_/\\ \n( o.o )\n > ^ < "

choices = {1: rat, 2: hunter, 3: lion}
points = {"p": 0, "c": 0}


def getName():
    name = input("Enter Player name: ")
    return name


def getChoice(r=0):
    c = int(input(f"{r}'s choice (1/rat, 2/hunter and 3/lion): "))

    if c <= 0 or c > 3:
        c = getChoice(r)

    return c


def cal(p, c, points):
    if p == 1 and c == 2:
        points["p"] += 1
    elif p == 2 and c == 3:
        points["p"] += 1
    elif p == 3 and p == 1:
        points["p"] += 1
    elif p == c:
        return
    else:
        points["c"] += 1


def play():
    name = "GAME"
    for i in range(5):
        p_choice = getChoice(i + 1)
        print(f"{name}")
        print(choices[p_choice])
        print("VS")
        print("Com")
        c_choice = random.randint(1, 3)
        print(choices[c_choice])
        cal(p_choice, c_choice, points)
        print(f"{name} {points['p']} / Com {points['c']}")
        if points["p"] == 3:
            print(f"{name} win.")
            return
        elif points["c"] == 3:
            print("Com win.")
            return

    if points["p"] == points["c"]:
        print("Draw!")
    elif points["c"] > points["p"]:
        print("Com win.")
    else:
        print(f"{name} win.")


play()
