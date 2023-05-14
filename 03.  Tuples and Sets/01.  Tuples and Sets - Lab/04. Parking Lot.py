lot = set()

for _ in range(int(input())):
    direction, plate = input().split(", ")
    if direction == "IN":
        lot.add(plate)
    if direction == "OUT":
        lot.remove(plate)

if not lot:
    print("Parking Lot is Empty")
else:
    print(*lot, sep="\n")
