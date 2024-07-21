def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


k = int(input("Input k: "))
arr = []
for i in range(1, k + 1):
    f = factorial(i)
    print(f"{i}! = {f}")
    arr.append(f)
print(f"Summation of factorial 1! - {k}! = {sum(arr)}")
