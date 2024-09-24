c_d = 100
p_d = 0
n = 0


def f(x):
    return 2**x


while p_d < c_d:
    dis = int(input("Input distance: "))
    n += 1
    c_d += f(n)
    p_d += dis
    print("Police distance:", p_d)
    print("Criminal distance:", c_d)
print("Caught him!")
