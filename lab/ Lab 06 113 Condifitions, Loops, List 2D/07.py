direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# matrix = []

# for _ in range(size):
#     row = list(map(int, input().split()))
#     matrix.append(row)
matrix = [
    [1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1],
    [1, 2, 3, 2, 1],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1],
]

s = size // 2
for i in range(s):
    l = size - i - 1
    if direction == "V":
        matrix[i], matrix[l] = matrix[l], matrix[i]
    elif direction == "H":
        matrix[i] = matrix[i][::-1]
        matrix[l] = matrix[l][::-1]

if size % 2 != 0:
    matrix[s] = matrix[s][::-1]


if size > 0:

    print("After flip:")
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
