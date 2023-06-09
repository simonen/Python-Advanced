bowls = list(map(int, input().split(", ")))
customers = list(map(int, input().split(", ")))

while bowls and customers:
    ramen = bowls.pop()
    customer = customers.pop(0)
    if ramen > customer:
        ramen -= customer
        bowls.append(ramen)
    elif ramen < customer:
        customer -= ramen
        customers.insert(0, customer)

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
else:
    print("Great job! You served all the customers.")

    if bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")