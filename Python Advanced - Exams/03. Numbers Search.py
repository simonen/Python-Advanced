def numbers_searching(*nums):
    duplicates = set(x for x in nums if nums.count(x) > 1)
    asc_duplicates = sorted(duplicates)
    asc_nums = sorted(nums)
    missing = 0

    for i in range(len(nums)):
        if asc_nums[i + 1] - asc_nums[i] > 1:
            missing = asc_nums[i] + 1
            return [missing, asc_duplicates]


print(numbers_searching(1, 3))
print('---------')
print(numbers_searching(1, 2, 4, 2, 5, 4))
print('---------')
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print('---------')
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

