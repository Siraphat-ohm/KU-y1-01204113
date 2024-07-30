def commaCode(l):
    length = len(l)
    if not length:
        return ""
    last = l.pop()
    if length > 1:
        return ", ".join(l) + ", and " + last
    else:
        return last


l = input("Input: ").split()
print(commaCode(l))
