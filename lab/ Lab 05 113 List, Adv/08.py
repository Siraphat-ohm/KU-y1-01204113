n = int(input("N: "))
m = int(input("M: "))
dis = set()
for i in range(n):
    num = int(input(f"Input number {i+1}: "))
    dis.add(num % m)

print(len(dis))
