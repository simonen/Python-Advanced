def multiply(*args):
    res = 1
    for i in args:
        res *= i
    return res


print(multiply(1, 2, 3, 4, 5, 6))
