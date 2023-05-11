robots = input().split(";")
busy_robots = {}
for x in robots:
    key = x.split("-")[0]
    if key not in busy_robots:
        busy_robots[key] = 0

command = input()
product_queue = []
while command != 'End':
    product = command
    product_queue.append(product)
    command = input()

start_time = input().split(":")
hh, mm, ss = start_time
total_seconds = int(hh) * 3600 + int(mm) * 60 + int(ss)
seconds = 0
while len(product_queue) > 0:
    total_seconds += 1
    seconds += 1
    hh = (total_seconds // 3600) % 24
    mm = (total_seconds // 60) % 60
    ss = total_seconds % 60

    product = product_queue.pop(0)
    for k, v in busy_robots.items():
        if busy_robots[k] != 0:
            busy_robots[k] -= 1

    for x in robots:
        index = robots.index(x)
        name = robots[index].split("-")[0]
        processing = int(robots[index].split("-")[1])
        if busy_robots[name] == 0:
            busy_robots[name] = processing
            print(f"{name} - {product} [{hh:0>2}:{mm:0>2}:{ss:0>2}]")
            break
    else:
        product_queue.append(product)
