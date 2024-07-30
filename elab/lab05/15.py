def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + " "
    return text


print("Parse a long paragraph (or text) below, following an ENTER as needed:")
text = getMultilinesInput()
k = int(input("Top K rank: "))

dictionary = {}

for word in text.lower().split():
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
d = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
ranks = []
rank = []
i = 1


c = 1
while i < len(d):
    if len(ranks) == k:
        break

    if d[i][1] == d[i - 1][1]:
        c += 1
    else:
        # print(i - 1, c)
        if c == 1:
            ranks.append(d[i - 1 : i])
        else:
            ranks.append(d[i - c : i])
        c = 1
    i += 1

if len(ranks) != k:
    ranks.append(d[i - c : i])
print(ranks)

for r in ranks:
    for i, l in enumerate(r):
        w, c = l
        if i == len(r) - 1:
            print(f"{w}: {c}", end="")
        else:
            print(f"{w}: {c}", end=", ")
    print()
