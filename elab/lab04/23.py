strings = input("Enter list of words: ").split()
c = 0
for word in strings:
    for ch in word:
        if ch.islower():
            c += 1

print(c)
