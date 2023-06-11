customers = list(map(int, input().split(", ")))
taxis = list(map(int, input().split(", ")))

total_time = 0

while customers and taxis:
    customer = customers.pop(0)
    taxi = taxis.pop()

    if customer <= taxi:
        total_time += customer
    else:
        customers.insert(0, customer)

if customers:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customers))}')
else:
    print('All customers were driven to their destinations')
    print(f"Total time: {total_time} minutes")