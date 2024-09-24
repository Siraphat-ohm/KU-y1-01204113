def change(n, b):
    return n // b


money = 1218

b500 = change(money, 500)
left = money - b500 * 500
b100 = change(left, 100)
left = left - b100 * 100
b20 = change(left, 20)
left = left - b20 * 20
b5 = change(left, 5)
left = left - b5 * 5
b1 = change(left, 1)
left = left - b1

print("500: %d" % b500)
print("100: %d" % b100)
print(" 20: %d" % b20)
print("  5: %d" % b5)
print("  1: %d" % b1)
