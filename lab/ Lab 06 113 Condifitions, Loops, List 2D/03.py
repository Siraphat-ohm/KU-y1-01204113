"""
Grid Size: 4 4
Number of mine(s): 3
Mine#1: 0 0
Mine#2: 1 2
Mine#3: 2 3
"""

m, n = tuple(map(int, input("Grid Size: ").split()))
n_mine = int(input("Number of mine(s): "))
mines = [tuple(map(int, input(f"Mine#{i+1}: ").split())) for i in range(n_mine)]
# m, n = (3, 4)
# mines = [(0, 0), (1, 2), (2, 2), (2, 0)]


def gen_map(mines, m, n):
    map = []
    for row in range(n):
        sub = []
        for col in range(m):
            if (col, row) in mines:
                sub.append("X")
            else:
                sub.append(0)
        map.append(sub)
    return map


def check_mine(x, y, map):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            if nx >= 0 and nx < n and ny >= 0 and ny < m and map[nx][ny] == "X":
                num += 1
    return num


map = gen_map(mines, m, n)
for i in range(n):
    for j in range(m):
        if map[i][j] != "X":
            print(check_mine(i, j, map), end=" ")
        else:
            print("X", end=" ")
    print()


"""
x, y
(x-1,y+1) (x,y) (x-1,y+1)
(x-1,y+1) (x,y)   (x,y+1)
(x-1,y+1) (x+1,y) (x+1,y+1)
"""
