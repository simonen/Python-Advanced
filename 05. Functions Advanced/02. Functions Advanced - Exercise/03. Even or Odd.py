def even_odd(*numbers):
    command = numbers[-1]
    nums = {'even': [int(x) for x in numbers[:-1] if int(x) % 2 == 0],
             'odd': [int(x) for x in numbers[:-1] if int(x) % 2 != 0]}

    return nums[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

