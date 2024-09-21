"""-------------------------------------------
 - Do not send this part of code!
 - No import command is allowed anywhere!
-------------------------------------------"""


def readMat(fn="gauss01.txt"):
    m = []
    with open(fn) as fp:
        for line in fp:
            m.append(line.strip().split(" "))
    return m


def printMat(m):
    for i in range(len(m)):
        row = ""
        for j in range(len(m[0])):
            row += f"{m[i][j]:>8}"
        print(row)
    print()


"""-------------------------------------------
 END: Do not send this part of code!
-------------------------------------------"""
# filename = "./testcase/gauss02.txt"

filename = input("Enter filename: ")
m = readMat(filename)
print("Augmented Matrix:")
printMat(m)


class Fraction:
    def __init__(self, n, d=1):
        if d < 0:
            n = -n
            d = -d
        c_d = gcd(abs(n), abs(d))
        self.n = n // c_d
        self.d = d // c_d

    def __repr__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def __float__(self):
        return self.n / self.d

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.n * other.n, self.d * other.d)
        else:
            return Fraction(self.n * other, self.d)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.n * other.d - other.n * self.d,
                self.d * other.d,
            )
        else:
            return Fraction(self.n - other * self.d, self.d)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.n * other.d, self.d * other.n)
        else:
            return Fraction(self.n, self.d * other)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.n == other.n and self.d == other.d
        else:
            return self.n == other * self.d

    def __neg__(self):
        return Fraction(-self.n, self.d)

    def __format__(self, format_spec):
        return f"{self.__repr__():{format_spec}}"


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def leadingOne(i, v):
    global m
    for k in range(len(m[i])):
        m[i][k] = m[i][k] / v


def subRow(i, o):
    global m
    for k in range(len(m[0])):
        m[i][k] = m[i][k] - o[k]


def back_substitution(m):
    num_rows = len(m)
    num_cols = len(m[0])
    x = [Fraction(0) for _ in range(num_cols - 1)]

    for i in range(num_rows - 1, -1, -1):
        rhs = m[i][-1]
        for j in range(i + 1, num_cols - 1):
            rhs -= m[i][j] * x[j]
        x[i] = rhs / m[i][i]

    return x


m = [[Fraction(int(col)) for col in row] for row in m]

length = len(m[0]) - 1

for i in range(length):
    nR = i + 1
    print(f"R{nR} => R{nR}/({m[i][i]})")
    leadingOne(i, m[i][i])
    printMat(m)
    for j in range(i + 1, length):
        vC = m[j][i]
        mul = [vC * c for c in m[i]]
        if vC != 0:
            print(f"R{nR}'->({vC})*R{nR} {mul}")
            print(f"R{j+1} ==> R{j+1}-R{nR}'")
            subRow(j, mul)
            printMat(m)

print("Result from Gaussian Elimination:")
printMat(m)

letter = "abcdefghijklmnopqrstuvwxyz"
solution = back_substitution(m)
print("After Back-Substitution:")
for i, v in enumerate(solution):
    print(letter[i], "=", v)
