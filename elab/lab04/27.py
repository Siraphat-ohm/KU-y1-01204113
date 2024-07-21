arr = eval(input("InputList: "))


n = len(arr)

ans = []
sub = [arr[0]]


for i in range(1, n):
    if arr[i - 1] == arr[i]:
        sub.append(arr[i])
    else:
        ans.append(sub)
        sub = [arr[i]]
ans.append(sub)

print(ans)
