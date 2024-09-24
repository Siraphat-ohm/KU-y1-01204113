a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
lst = [a, b, c]


while sum(lst) != 1:
    a, b, c = lst
    if a >= c and b >= c:
        lst[0] -= 1
        lst[1] -= 1
        lst[2] += 1
    elif a >= b and c >= b:
        lst[0] -= 1
        lst[1] += 1
        lst[2] -= 1
    elif b >= a and c >= a:
        lst[0] += 1
        lst[1] -= 1
        lst[2] -= 1


ans = "ABC"


print(ans[lst.index(max(lst))])
