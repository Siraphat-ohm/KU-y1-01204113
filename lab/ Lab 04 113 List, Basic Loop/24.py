arr = [int(n) for n in input("Enter list of number: ").split()]
# arr = [0, -3, -5, -7, -8]
# arr = [0, 3, 4, 7, 9]


def find_pairs(nums):
    pairs = []
    length = len(nums)
    for n in range(length):
        if arr[n] - 3 in nums:
            # print(n, n - 3)
            pairs.append([arr[n], arr[n] - 3])
        elif arr[n] + 3 in nums:
            # print(n, n + 3)
            pairs.append([arr[n], arr[n] + 3])
        # nums[n] = None

    return pairs


def find_pairs_brute_force(nums):
    pairs = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(nums[i] - nums[j]) == 3:
                pairs.append([nums[i], nums[j]])

    return pairs


# print(f"Output list: {find_pairs(arr)}")
print(f"Output list: {find_pairs_brute_force(arr)}")
