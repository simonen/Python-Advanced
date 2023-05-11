clothes = input().split()
rack_cap = int(input())

racks = 1
rack = rack_cap
while clothes:
    if rack >= int(clothes[-1]):
        cloth = int(clothes.pop())
        rack -= cloth
    else:
        rack = rack_cap
        racks += 1

print(racks)
