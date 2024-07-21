import string


def encrypt(text, shift):
    enc = ""
    offset = 0
    for e in text:
        ascii = ord(e)
        if ascii >= 97:
            letters = string.ascii_lowercase
            offset = 97
        else:
            letters = string.ascii_uppercase
            offset = 65
        if e.isalpha():
            enc += letters[(ord(e) - offset + shift) % 26]
        else:
            enc += e

    return enc


text = input("Enter text: ")
shift = int(input("Enter step: "))
print(encrypt(text, shift))
