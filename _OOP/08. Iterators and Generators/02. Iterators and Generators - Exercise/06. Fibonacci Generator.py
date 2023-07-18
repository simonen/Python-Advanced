def fibonacci():
    nums = [0, 1]
    i = 0
    count = 0
    while True:
        if i < 2:
            yield nums[i]
            count += 1
        nums.append(sum(nums[i:i + 2]))
        yield sum(nums[i:i + 2])
        i += 1


generator = fibonacci()
for i in range(20):
    print(next(generator))
