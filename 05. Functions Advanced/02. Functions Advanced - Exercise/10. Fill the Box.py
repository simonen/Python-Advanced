def fill_the_box(height, length, width, *cubes):
    box_vol = height * length * width
    cubes = list(cubes)
    while True:
        if cubes[0] == "Finish":
            break
        if cubes[0] > box_vol:
            cubes[0] -= box_vol
            box_vol = 0
            break
        cube = cubes.pop(0)
        box_vol -= cube

    if box_vol > 0:
        return f"There is free space in the box. You could put {box_vol} more cubes."

    return f"No more free space! You have {sum(x for x in cubes if isinstance(x, int))} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
