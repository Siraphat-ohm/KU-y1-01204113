arr = eval(input("InputList: "))
out = []
for i in range(len(arr)):
    if arr[i] != arr[i - 1]:
        out.append(arr[i])
print(out)
