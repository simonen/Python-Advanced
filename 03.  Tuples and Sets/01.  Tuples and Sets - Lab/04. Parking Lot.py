lot = set()

for _ in range(int(input())):
    direction, plate = input().split(", ")
    if direction == "IN":
        lot.add(plate)
    if direction == "OUT":
        lot.remove(plate)

if len(lot) == 0:
    print("Parking Lot is Empty")
else:
    [print(x) for x in lot]
