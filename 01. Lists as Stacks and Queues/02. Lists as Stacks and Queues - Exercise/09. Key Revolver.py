bullet_price = int(input())
barrel_size = int(input())
bullets = input().split()
locks = input().split()
value = int(input())

rounds = barrel_size
shots = 0
while bullets and locks:
    bullet = bullets.pop()
    rounds -= 1
    shots += 1

    if int(bullet) > int(locks[0]):
        print("Ping!")
    else:
        print("Bang!")
        locks.pop(0)

    if rounds == 0 and len(bullets) > 0:
        print("Reloading!")
        rounds = barrel_size

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value - shots * bullet_price}")
