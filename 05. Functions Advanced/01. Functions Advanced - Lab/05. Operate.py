def operate(operator, *args):

    def add():
        return sum(args)

    def subtract():
        res = args[0]
        for i in range(1, len(args)):
            res -= args[i]
        return res

    def multiply():
        res = 1
        for i in args:
            res *= i
        return res

    def divide():
        res = args[0]
        for i in range(1, len(args)):
            if args[i] != 0:
                res /= args[i]
        return res

    if operator == "+":
        return add()

    elif operator == "-":
        return subtract()

    elif operator == "*":
        return multiply()

    elif operator == "/":
        return divide()


print(operate("/", 5, 4))