class Fraction:
    def __init__(self, n, d):
        gcd = self._gcd(n, d)
        self.n = n // gcd
        self.d = d // gcd

    def _gcd(self, x, y):
        while y:
            temp = y
            y = x % y
            x = temp
        return abs(x)

    def __add__(self, other):
        d = self.d * other.d
        n = self.n * other.d + other.n * self.d
        return Fraction(n, d)

    def add(self, num):
        return Fraction(self.n, self.d) + Fraction(num, 1)

    def __mul__(self, other):
        d = self.d * other.d
        n = self.n * other.n
        return Fraction(n, d)

    def evaluate(self):
        return self.n / self.d

    def multiply(self, num):
        return Fraction(self.n * num, self.d)

    def __toString__(self):
        return f"{self.n} / {self.d}"

    def __str__(self):
        return f"{self.n} / {self.d}"


# print(Fraction(22, 7).multiply(7).multiply(7))
# print((Fraction(22, 14) * Fraction(2, 4)).add(1))
# print((Fraction(1, 2) + Fraction(3, 4)).multiply(0))
