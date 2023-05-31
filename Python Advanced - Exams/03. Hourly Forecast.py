def forecast(*args):
    book = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    for city, weather in args:
        book[weather].append(city)

    locations = []
    weathers = []
    res = []

    for weather, location in book.items():
        locations.append(sorted(location))
        weathers.append(weather)

    for i in range(3):
        for city in locations[i]:
            res.append(f"{city} - {weathers[i]}")

    return "\n".join(res)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))