class Coin:
    def __init__(self, value=1):
        self.value = value

    def __str__(self):
        return f"{self.value} Baht Coin"


class BankNote:
    def __init__(self, value=20):
        self.value = value

    def __str__(self):
        return f"{self.value} Baht Banknote"


# amount = 15394
amount = int(input("Input amount : "))

banks = [
    BankNote(1000),
    BankNote(500),
    BankNote(100),
    BankNote(50),
    BankNote(20),
]

coins = [Coin(10), Coin(5), Coin(2), Coin(1)]

for b in banks:
    n = amount // b.value
    amount %= b.value
    if n:
        print(f"You get {n} of", end=" ")
        print(b)

for c in coins:
    n = amount // c.value
    amount %= c.value
    if n:
        print(f"You get {n} of", end=" ")
        print(c)
