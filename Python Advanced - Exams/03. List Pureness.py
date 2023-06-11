def best_list_pureness(nums, k):
    res = []
    biggest = -1000000000
    for r in range(k + 1):
        num_sum = 0
        for i, d in enumerate(nums):
            num_sum += i * d

        if num_sum > biggest:
            biggest = num_sum
            res.append((biggest, r))

        nums.insert(0, nums.pop())

    pureness = sorted(res, key=lambda x: -x[0])
    purest = pureness[0][0]
    rotations = pureness[0][1]

    return f"Best pureness {purest} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
#
# print('-' * 22)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
#
# print(result)
# print('-' * 22)
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
#
# print(result)
print('-' * 22)
test = ([5, 1, 1], 1)
result = best_list_pureness(*test)

print(result)