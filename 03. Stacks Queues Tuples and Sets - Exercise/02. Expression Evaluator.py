from functools import reduce
import operator


funcs = {"+": lambda *args: sum(args),
         "-": lambda *args: args[0] - sum(args[1:]),
         "*": lambda *args: reduce(operator.mul, args, 1),
         "/": lambda *args: reduce(operator.floordiv, args)}

numbers = input().split()
operators = "+-*/"
curr_res = None
start = 0
num_args = []
last_res = []

for i in range(len(numbers)):
    last_res = [curr_res] if curr_res is not None else []
    if numbers[i] in operators:
        curr_operator = numbers[i]
        num_args = last_res + list(map(int, numbers[start:i]))
        start = i + 1
        curr_res = funcs[curr_operator](*num_args)

print(curr_res)
