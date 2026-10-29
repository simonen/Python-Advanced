from collections import deque


green_light, free_window = int(input()), int(input())
command = input()
car_queue = deque()
crashes = []
transiting = []
cars_passed = []

while command != "END":
    if command != "green":
        car_queue.append(command)
        command = input()
        continue

    green_timer = green_light
    free_timer = free_window

    while green_timer > 0 and car_queue:
        car = car_queue.popleft()
        if len(car) <= green_timer:
            cars_passed.append(car)
            green_timer -= len(car)
        else:
            transiting.append(car)

    if transiting:
        free_timer += green_timer
        if len(car) <= free_timer:
            cars_passed.append(car)
            transiting = []
        else:
            hit = car[free_timer]
            crashes.append((car, hit))
            print(f"A crash happened!\n{car} was hit at {hit}.")
            break

    command = input()

if not crashes:
    print(f"Everyone is safe.\n{len(cars_passed)} total cars passed the crossroads.")
