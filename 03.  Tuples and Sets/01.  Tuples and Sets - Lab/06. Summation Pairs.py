import time

digits = set(input().split())
target = int(input())
start_time = time.time()

while digits:
    a = digits.pop()
    for i in digits:
        if int(i) + int(a) == target:
            print(f"{a} + {i} = {target}")

print("--- %s seconds ---" % (time.time() - start_time))


print(digits)