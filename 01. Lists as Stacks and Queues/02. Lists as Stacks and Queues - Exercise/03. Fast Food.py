from collections import deque

quantity = int(input())
orders = deque(input().split())
print(max(int(x) for x in orders))

if quantity >= sum(int(x) for x in orders):
    print("Orders complete")
    orders = []

while orders:
    if quantity < int(orders[0]):
        break

    quantity -= int(orders[0])
    orders.popleft()


if orders:
    print(f"Orders left: {' '.join(orders)}")
