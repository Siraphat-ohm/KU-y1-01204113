s1 = input("Input string: ")
s2 = input("Input string: ")


def uncommon(s1, s2):
    out = ""
    for ch in s1:
        if ch not in s2:
            out += ch
    return out


print(uncommon(s1, s2) + uncommon(s2, s1))
