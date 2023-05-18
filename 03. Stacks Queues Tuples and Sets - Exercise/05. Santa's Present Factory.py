materials = input().split()
magic_level = input().split()

toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.pop(0)
    total_magic = int(material) * int(magic)
    if int(material) == 0 and int(magic) == 0:
        continue
    if total_magic > 0:
        if total_magic in toys:
            if toys[total_magic] not in presents:
                presents[toys[total_magic]] = 0
            presents[toys[total_magic]] += 1
        else:
            materials.append(str(int(material) + 15))
    elif total_magic < 0:
        total_magic = int(material) + int(magic)
        materials.append(str(total_magic))
    elif int(material) == 0:
        magic_level.insert(0, magic)
    elif int(magic) == 0:
        materials.append(material)

if "Doll" in presents and "Wooden train" in presents or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(magic_level)}")

for toy, count in sorted(presents.items(), key=lambda x: x):
    print(f"{toy}: {count}")
