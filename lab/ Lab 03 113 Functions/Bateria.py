def nb_year(p0, percent, aug, p):
    n = 0
    bateria = 0

    percent /= 100
    while bateria < p:
        n += 1
        bateria = int(p0 + p0 * percent + aug)
        p0 = bateria
    return n


print(nb_year(1000, 2, 30, 1150))
print(nb_year(0, 0, 0, 1000))
