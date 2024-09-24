n, m = list(map(int, input().split()))

times = [int(input()) for _ in range(n)]

kill = 0
mt = max(times) * m
for t in range(1, mt):
    if kill >= m:
        print(t - 1)
        break

    for i in times:
        if t % i == 0:
            kill += 1
