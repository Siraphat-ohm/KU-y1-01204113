strings = input("Enter a set of strings: ").split()


def countStr(strings):
    c = 0
    for s in strings:
        if len(s) >= 2:
            if s[0] == s[-1]:
                c += 1
    return c


print(countStr(strings))
