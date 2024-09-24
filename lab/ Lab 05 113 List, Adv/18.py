s1 = eval(input("String set1: "))
# s1 = ["abcdefgh", "geeksforgeeks", "lmnopqrst", "abc"]
s2 = eval(input("String set2: "))
# s2 = ["ijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]


def f(l):
    length = len(l)
    o = [0] * 26

    for i in l:
        id = ord(i) % 26
        if o[id] == 0:
            o[id] = 1
    return o


o = []
c = 0
for w1 in s1:
    for w2 in s2:
        s = w1 + w2
        if sum(f(s.lower())) == 26:
            o.append(s)
            c += 1

print("Output:", c)
print("The total complete pairs that are forming are:")
for s in o:
    print(f" {s}")
