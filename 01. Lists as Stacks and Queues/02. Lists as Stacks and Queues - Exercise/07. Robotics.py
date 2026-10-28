from collections import deque


def time_convert(time_s: int) -> str:
    ss = int(time_s) % 60
    hh = int(time_s) // 3600 % 24
    mm = int(time_s) // 60 % 60
    return f"{hh:0>2}:{mm:0>2}:{ss:0>2}"

robots = input().split(";")
busy_robots = {x.split("-")[0]: 0 for x in robots}
start_time = input().split(":")
total_seconds = int(start_time[0]) * 3600 + int(start_time[1]) * 60 + int(start_time[2])
product_queue = deque()

command = input()
while command != 'End':
    product_queue.append(command)
    command = input()

while product_queue:
    total_seconds += 1
    product = product_queue.popleft()

    for key in busy_robots:
        if busy_robots[key] > 0:
            busy_robots[key] -= 1

    for i, robot in enumerate(robots):
        name, processing = robots[i].split("-")
        if busy_robots[name] == 0:
            busy_robots[name] = int(processing)
            print(f"{name} - {product} [{time_convert(total_seconds)}]")
            break
    else:
        product_queue.append(product)
