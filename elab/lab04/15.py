arr = []
# arr = [2, 5, 5, 5, 5, 3, 5, 8, 5, 5]
# arr = [-2, 7, -2, 100, -2, -2, -2, -2, 5]
# arr = [2, 7, 7, 7, 3, 2, 2, 2]
# arr = [5, 2, -2, 7, 8, 9, 10]

while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)

n = len(arr)

ans = []

c = 1
current = arr[0]
max = 1

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        c += 1
        current = arr[i]
    else:
        if c >= max:
            max = c
            ans.append([current, max])
            c = 0
ans.append([current, max])

print(ans[0][1])
print(ans[0][0])
