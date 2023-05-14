import time

digits = list(range(10000))
target = 2500
start_time = time.time()
count = 0
while digits:
    a = digits.pop()
    for i in digits:
        if int(i) + int(a) == target:
            print(f"{a} + {i} = {target}")
            count += 1


end = time.time()
print(f"Time: {end-start_time}")
print(count)
