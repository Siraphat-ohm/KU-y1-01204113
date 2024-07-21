def myzip(m, n):

    if len(m) != len(n):
        return []
    return [m[i] + n[i] for i in range(len(m))]
