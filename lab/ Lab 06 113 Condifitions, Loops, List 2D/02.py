s = input("Input sentence: ")
rows = int(input("Input row: "))

enc = [""] * rows

i, direction = 0, -1
for ch in s:
    enc[i] += ch
    if i == 0 or i == rows - 1:
        direction *= -1
    i += direction
print("".join(enc))
