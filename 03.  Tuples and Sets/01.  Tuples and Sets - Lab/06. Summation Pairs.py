digits = input().split()
target = int(input())

while digits:
    digit = int(digits.pop(0))
    for d in digits:
        if digit + int(d) == target:
            print(f"{digit} + {d} = {target}")

