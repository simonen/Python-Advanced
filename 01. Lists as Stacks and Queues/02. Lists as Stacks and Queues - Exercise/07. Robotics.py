robots = input().split(";")
robots.append("Busy")
busy_robots = []
# print(robots)
start_time = input().split(":")
command = input()
product_queue = []
while command != 'End':
    product = command
    product_queue.append(product)
    command = input()

# print(product_queue)
seconds = 0
hh, mm, ss = start_time
total_seconds = int(hh) * 3600 + int(mm) * 60 + int(ss)
free_at = 0
bot = ''
while len(product_queue) > 0:
    total_seconds += 1
    seconds += 1
    hh = (total_seconds // 3600) % 24
    mm = (total_seconds // 60) % 60
    ss = total_seconds % 60

    for i in range(len(busy_robots)):
        name = busy_robots[i].split("-")[0]
        processing = int(busy_robots[i].split("-")[1])
        processing -= 1
        busy_robots[i] = f"{name}-{processing}"
        if int(busy_robots[i].split("-")[1]) == 0:
            bot = busy_robots.pop(i)
            busy_robots.append(bot)
            for j in robots:
                if j.split("-")[0] == bot.split("-")[0]:
                    bot = j
            robots.pop(robots.index(bot))
            robots.insert(0, bot)
    if int(busy_robots[-1].split("-")[1]) == 0:
        while int(busy_robots[-1].split("-")[1]) == 0:
            busy_robots.pop(-1)
    name = robots[0].split("-")[0]
    if not any(name in x.split("-")[0] for x in busy_robots):
        busy_robots.append(robots[0])
        robots.append(robots.pop(0))
        product = product_queue.pop(0)
        print(f"{name} - {product} [{hh:0>2}:{mm:0>2}:{ss:0>2}]")
        continue
    else:
        product_queue.append(product_queue.pop(0))




