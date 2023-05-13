robots = input().split(";")
start_time = input().split(":")

command = input()
product_queue = []
while command != 'End':
    product = command
    product_queue.append(product)
    command = input()

busy_robots = {x.split("-")[0]: 0 for x in robots}
hh, mm, ss = start_time
total_seconds = int(hh) * 3600 + int(mm) * 60 + int(ss)

while len(product_queue) > 0:
    total_seconds += 1
    hh = (total_seconds // 3600) % 24
    mm = (total_seconds // 60) % 60
    ss = total_seconds % 60

    for key in busy_robots:
        if busy_robots[key] != 0:
            busy_robots[key] -= 1

    product = product_queue.pop(0)
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
