n = int(input())

pumps = []
tank = 0
for i in range(n):
    stop = list(map(int, input().split()))
    fill, distance = stop
    tank += fill
    if distance <= tank:
        pumps.append(i)
        tank -= distance
    else:
        tank = 0
        pumps = []

print(pumps[0])
