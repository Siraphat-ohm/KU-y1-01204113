def simple_interest(p, r, t):
    r = r / 100
    return p + p * r * t


def compound_interest(p, r, t):
    r = r / 100
    return p * (1 + r) ** t


def readInput():
    p = float(input("Enter principle: "))
    r = float(input("Enter interest rate: "))
    t = float(input("Enter time: "))
    return (p, r, t)


p, r, t = readInput()

print(
    "Return money for simple interest calculation is %.2f Baht."
    % (simple_interest(p, r, t))
)
print(
    "Return money for compound interest calculation is %.2f Baht."
    % (compound_interest(p, r, t))
)
