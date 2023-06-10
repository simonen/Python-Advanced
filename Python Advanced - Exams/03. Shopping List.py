def shopping_list(budget, **kwargs):
    items = 0
    purchase = []
    shop_list = [x for x in kwargs]

    if budget < 100:
        return f"You do not have enough budget."

    while shop_list and items < 5:
        product = shop_list.pop(0)
        price = kwargs[product][0]
        quantity = kwargs[product][1]
        if quantity * price <= budget:
            purchase.append(f"You bought {product} for {(price * quantity):.2f} leva.")
            budget -= quantity * price
            items += 1

    return '\n'.join(purchase)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print('-----------')
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print('-----------')
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))