l1 = eval(input("Input list1: "))
l2 = eval(input("Input list2: "))

if len(l1) < len(l2):
    temp = l1
    l1 = l2
    l2 = temp

m = []
a = []

for i in l1:
    if i not in l2:
        a.append(i)

for i in l2:
    if i not in l1:
        m.append(i)

# print(a)
# print(m)
print(f"Missing values in list1 = {m}")
print(f"Additional values in list1 = {a}")
print(f"Missing values in list2 = {a}")
print(f"Additional values in list2 = {m}")
