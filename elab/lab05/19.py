s = input("Enter a string: ").lower().split()

s = "".join(s)

vowels = []
consonants = []


for i in s:
    if i in ("a", "e", "i", "o", "u") and i not in vowels:
        vowels.append(i)
    elif i not in consonants and i not in vowels and i.isalpha():
        consonants.append(i)

print("Unique vowels: ", vowels)
print("Unique consonants: ", consonants)
