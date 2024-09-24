from math import ceil

numbers = list(map(int, input().split()))

print(ceil(sum(numbers) / 4))
