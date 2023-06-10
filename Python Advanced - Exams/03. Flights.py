def flights(*args):
    book = {}

    for i in range(0, len(args), 2):
        if args[i] == "Finish":
            break

        city = args[i]
        passangers = int(args[i + 1])

        if city not in book:
            book[city] = 0
        book[city] += passangers

    return book


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print("--------------------")
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print("--------------------")
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))