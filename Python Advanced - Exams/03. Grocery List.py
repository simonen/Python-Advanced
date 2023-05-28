def shop_from_grocery_list(budget, groceries, *prices):
    prices = list(prices)
    for item in prices:
        product = item[0]
        price = item[1]
        if product in groceries and price <= budget:
            budget -= price
            groceries.pop(groceries.index(product))

        if price > budget:
            break

    if groceries:
        return f"You did not buy all the products. Missing products: {', '.join(groceries)}."

    return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))