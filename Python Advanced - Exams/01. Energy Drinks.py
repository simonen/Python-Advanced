caffeine = list(map(int, input().split(", ")))
drinks = list(map(int, input().split(", ")))

total_intake = 0
max_intake = 300

while caffeine and drinks:
    caffe = caffeine.pop()
    drink = drinks.pop(0)
    intake = caffe * drink
    if intake <= max_intake - total_intake:
        total_intake += intake
    else:
        drinks.append(drink)
        if total_intake >= 30:
            total_intake -= 30

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_intake} mg caffeine.")
