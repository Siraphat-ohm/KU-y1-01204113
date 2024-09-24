def countConsec(l):
    i = 1
    c = 1
    e = l[i - 1]
    ans = []

    length = len(l)
    ans = []
    while i < length:
        if e == l[i]:
            c += 1
        else:
            ans.append((e, c))
            c = 1
        i += 1
        e = l[i - 1]
    ans.append((e, c))

    return ans


l = eval(input("Enter a list of objects: "))

if l:
    cs = countConsec(l)

    e, c = max(cs, key=lambda x: x[1])

    print(e)
    print(c)
else:
    print("Nothing to do.")
