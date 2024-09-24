arr = [
    tuple(int(k) for k in " ".join(i).split())
    for i in input("Enter list of tuple: ").split()
]

print(f"Input list: {arr}")
arr_s = sorted(arr, key=lambda x: x[-1])
print(f"Output list: {arr_s}")
