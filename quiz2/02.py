def swap(i, j):
    temp = i
    i = j
    j = temp
    return i, j


def bsort(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i] < l[j]:
                l[j], l[i] = swap(l[j], l[i])
    return l


def cmp(e1, e2):
    if e1 < e2:
        return True

    return False


def merge(l1, l2):
    l1 = bsort(l1)
    l2 = bsort(l2)
    i = 0
    j = 0
    ans = []
    while j < len(l2) and i < len(l1):
        if cmp(l1[i], l2[j]):
            ans.append(l1[i])
            i += 1
        else:
            ans.append(l2[j])
            j += 1
    while i < len(l1):

        ans.append(l1[i])
        i += 1
    while j < len(l2):
        ans.append(l2[j])
        j += 1
    return ans
