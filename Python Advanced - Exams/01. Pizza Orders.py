orders = list(map(int, input().split(", ")))
pizza_cap = list(map(int, input().split(", ")))
pizzas = 0

while orders and pizza_cap:
    order = orders.pop(0)
    if order > 10:
        continue

    employee = pizza_cap.pop()

    if order <= 0:
        pizza_cap.append(employee)

    elif order <= employee:
        pizzas += order

    elif order > employee:
        if order <= 10:
            order -= employee
            pizzas += employee
            orders.insert(0, order)

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas}')
    if pizza_cap:
        print(f'Employees: {", ".join(map(str, pizza_cap))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, orders))}')
