green_free = [int(input()), int(input())]
command = input()
cars = []
passed = 0
green = 0
window = 0

while command != 'END':
    if command != 'green':
        cars.append(command)
        command = input()
        continue

    green, window = green_free
    rem = ''
    car = ''
    while green > 0 and len(cars) > 0:
        car = cars[0]
        cars[0] = cars[0][green:]
        green -= len(car)
        if cars[0] == '':
            passed += 1
        rem = cars.pop(0)

    if rem == '':
        command = input()
        continue

    if rem[window:] != '':
        hit = rem[window:][0]
        print("A crash happened!\n"
              f'{car} was hit at {hit}.')
        break

    passed += 1
    command = input()
else:
    print("Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")
