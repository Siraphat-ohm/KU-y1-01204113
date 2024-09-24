import re


def readInput():
    map = []
    g_pos = []
    e_pos = []
    n = int(input())
    for i in range(n):
        row = input()
        row = re.findall(r"\d+|\S", row)
        map.append(row)
        for j, v in enumerate(row):
            if v == "E":
                e_pos.append((i, j))
            if v == "G":
                g_pos.append((i, j))
    return map, g_pos, e_pos


def disMap(m):
    for row in m:
        for col in row:
            print(col, end="")
        print()

    return


def cal(x, y, b):
    s = [-2, -1, 0, 1, 2]

    res = []
    for r in s:
        for c in s:
            nx = x + r
            ny = y + c
            if nx >= 0 and ny >= 0 and nx < b and ny < b:
                res.append((nx, ny))
    return res


map, g_pos, e_pos = readInput()

c = 0
for gx, gy in g_pos:

    l = cal(gx, gy, len(map[0]))

    for i in range(len(e_pos)):
        if e_pos[i] in l:
            c += 1
            e_pos[i] = None

print(c)


"""
0 1 2
. . G 0
. . . 1
. . . 2

[
    (0,2), (0,1), (0,0),
    (1,2), (1,1), (1,0),
    (2,2), (2,1), (2,0)
]

"""


"""
  0 1 2 3 4
0 # # # # #
1 # # # # #
2 # # G # #
3 # # # # #
4 # # # # #

(2,2)
(x,y)

[
 (x-2,y-2), (x-2,y-1), (x-2,y),  (x-2,y+1), (x-2,y+2),
 (x-1,y-2), (x-1,y-1), (x-1,y),  (x-1,y+1), (x-1,y+2),
 (x  ,y-2), (x,y-1),       #  ,  (x  ,y+1), (x  ,y+2),
 (x+1,y-2), (x+1,y-1), (x+1,y),  (x+1,y+1), (x+1,y+2),
 (x+2,y-2), (x+2,y-1), (x+2,y),  (x+1,y+1), (x+2,y+2)
]
"""

# map, g_pos, e_pos = (
#     [
#         ["G", ".", "E", ".", ".", ".", "E"],
#         ["E", ".", ".", ".", ".", ".", "."],
#         [".", ".", ".", ".", ".", ".", "G"],
#         [".", ".", ".", ".", ".", ".", "."],
#         [".", ".", ".", ".", "E", ".", "."],
#         [".", ".", ".", ".", ".", ".", "."],
#         ["E", ".", ".", ".", ".", ".", "."],
#     ],
#     [(0, 0), (2, 6)],
#     [(0, 2), (0, 6), (1, 0), (4, 4), (6, 0)],
# )

# map, g_pos, e_pos = (
#     [
#         ["G", ".", ".", ".", "E"],
#         [".", ".", ".", ".", "."],
#         [".", ".", ".", ".", "."],
#         ["E", ".", ".", ".", "."],
#         [".", ".", ".", ".", "."],
#     ],
#     [(0, 0)],
#     [(0, 4), (3, 0)],
# )
#
