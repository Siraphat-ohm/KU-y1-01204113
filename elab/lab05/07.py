num = int(input("Enter lucky number : "))
amount = int(input("Enter amount of candidates : "))

ids = {}


def count(id, num):
    c = 0
    num = str(num)
    for i in id:

        if i == num:
            c += 1
    return c


for i in range(amount):
    id = int(input(f"Enter ID card number {i+1}: "))
    ids[id] = count(str(id), num)

max = max(ids.values())

max_id = -1e10

for p, c in ids.items():
    if c == max and p >= max_id:
        max_id = p

print(f"Winner: {max_id}")
