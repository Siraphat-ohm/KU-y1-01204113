arr = eval(input("Original list: "))


def flattern(arr):
    l = []
    for e in arr:
        if isinstance(e, list):
            l.extend(flattern(e))
        else:
            l.append(e)

    return l


print(f"Flatten list: {flattern(arr)}")
