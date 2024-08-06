# words = "HEAD HEAP LEAP TEAR REAR BAER BAET BEEP JEEP JOIP JEIP AEIO".split()
# words = "SUN TON BOW GOD LOT KID FAX BAT FAT CAR EAT FEE SEA MAP DRY SPY TAP".split()

words = input("Text: ").split()


length = len(words)
c_chains = 1
c_words = 1
max_words = 0

d = 0
for i in range(1, length):
    d = 0
    for f, s in zip(words[i], words[i - 1]):
        if f != s:
            d += 1
    if d > 2:
        c_chains += 1
        c_words = 1
    if max_words < c_words:
        max_words = c_words
    c_words += 1

print(f"{c_chains} Chain(s). Maximum length is {max_words} word(s).")
