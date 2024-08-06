h, w = 0, 0

s_h = int(input("Enter horizontal shift size: "))
s_v = int(input("Enter vertical shift size: "))

image = []
print("Enter image:")

while True:
    row = []
    l = input()
    if l == "-1":
        break
    for s in l:
        row.append(s)
    image.append(row)

h = len(image)
w = len(image[0])


def isbound(i, x, y):
    if i >= x and i <= y:
        return False
    return True


def shift_h(shift, img, size):
    h, w = size
    res = []
    for i in range(h):
        s = []
        for j in range(w):
            if not isbound(j, shift, w):
                s.append(img[i][j - shift])
            else:
                s.append(0)
        res.append(s)
    return res


def shift_v(shift, img, size):
    h, w = size
    res = []
    for i in range(h):
        s = []
        for j in range(w):
            if not isbound(i, shift, w):
                s.append(img[i - shift][j])
            else:
                s.append(0)
        res.append(s)
    return res


def dis(img):
    for row in img:
        for col in row:
            print(col, end="")
        print()


print("After shift:")
dis(shift_v(s_v, shift_h(s_h, image, (h, w)), (h, w)))
