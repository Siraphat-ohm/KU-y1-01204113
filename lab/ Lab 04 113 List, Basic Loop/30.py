# arr = eval("[[1,3],[1,3],[13,15,17],[5,7],[9,11],[9,11],[9,11],[5,7]]")
arr = eval(input("Input: "))


count = {}

for i in arr:
    k = str(i)
    if k not in count:
        count[k] = 1
    else:
        count[k] += 1

count = sorted(count.items(), key=lambda x: x[1], reverse=True)

for k, v in count:
    print(f"{k}: {v}")
