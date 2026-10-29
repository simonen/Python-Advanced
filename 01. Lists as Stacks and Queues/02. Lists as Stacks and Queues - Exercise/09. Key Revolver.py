from collections import  deque


bullet_price = int(input())
barrel_size = int(input())
bullets = deque(list(map(int, input().split())))
locks = deque(list(map(int, input().split())))
value = int(input())
loaded_bullets = min(barrel_size, len(bullets))

while bullets and locks:
    bullet = bullets.pop()
    value -= bullet_price
    loaded_bullets -= 1
    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if loaded_bullets == 0 and bullets:
        print("Reloading!")
        loaded_bullets = min(barrel_size, len(bullets))

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value}")
