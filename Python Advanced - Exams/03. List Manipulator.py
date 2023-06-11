def list_manipulator(numbers, command, position, *nums):
    res = numbers
    if command == 'add' and position == "beginning":
        res = list(nums) + res
    elif command == "add" and position == "end":
        res.extend(nums)

    elif command == "remove" and position == "beginning":
        if nums:
            begin = nums[0]
            res = res[begin:]
        else:
            res.pop(0)

    elif command == "remove" and position == "end":
        if nums:
            begin = nums[0]
            res = res[:-begin]
        else:
            res.pop()

    return res


print(list_manipulator([1, 2, 3], "remove", "end"))
print('---------')
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print('---------')
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print('---------')
print(list_manipulator([1, 2, 3], "add", "end", 30))
print('---------')
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print('---------')
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print('---------')
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print('---------')
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
