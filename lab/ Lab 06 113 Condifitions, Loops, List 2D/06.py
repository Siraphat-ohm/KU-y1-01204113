directions = []

pos = tuple(map(int, input("City Size: ").split()))

city = [
    # [1, 1, 1, 1, 1],
    # [1, 2, 2, 2, 1],
    # [1, 2, 3, 2, 1],
    # [1, 2, 2, 2, 1],
    # [1, 1, 1, 1, 1],
]

for i in range(pos[0]):
    city.append(list(map(int, input().split())))


def h(city, pos):
    x, y = pos

    max = 0
    c = 0
    for j in range(x):
        for i in range(y):
            if max == 0:
                max = city[j][i]
            if max < city[j][i]:
                c += 1
                max = city[j][i]
        max = 0
    return c + x


def v(city, pos):
    x, y = pos

    max = 0
    c = 0
    for i in range(y):
        for j in range(x):
            if max == 0:
                max = city[j][i]
            if max < city[j][i]:
                c += 1
                max = city[j][i]
        max = 0
    return c + y


for i in range(4):
    n_map = []
    if i == 1:
        length = len(city)
        m = city.copy()

        for k in range(length // 2):
            l = length - k - 1
            m[k], m[l] = m[l], m[k]
        directions.append(m)
    elif i == 2:
        for row in city:
            n_map.append(row[::-1])
        directions.append(n_map)
    else:
        directions.append(city)

n, s, e, w = directions

ans = "NSEW"
ds = [v(n, pos), v(s, pos), h(e, pos), h(w, pos)]
max = max(ds)

k = 0
for i in ds:
    if i == max:
        print(ans[k], end=" ")
    k += 1
print()
