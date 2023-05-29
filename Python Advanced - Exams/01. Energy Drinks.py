caffeine = list(map(int, input().split(", ")))
drinks = list(map(int, input().split(", ")))

stamat = 0

while caffeine and drinks:
    caffe = caffeine.pop()
    drink = drinks.pop(0)
    caff_amount = caffe * drink
    if caff_amount <= 300 - stamat:
        stamat += caff_amount
    else:
        drinks.append(drink)
        if stamat >= 30:
            stamat -= 30
        else:
            stamat = 0

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat} mg caffeine.")
