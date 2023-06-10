def stock_availability(flavors, action, *args):
    inventory = flavors
    if action == "delivery":
        inventory.extend(args)
    elif action == 'sell':
        if not args:
            inventory.pop(0)
        for i in args:
            if isinstance(i, int):
                inventory = inventory[i:]
            elif isinstance(i, str):
                inventory = [x for x in inventory if x not in args]

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print("-------------")
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print("-------------")
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print("-------------")
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print("-------------")
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print("-------------")
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print("-------------")
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))