def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for i in range(1, n - 1):
        curr_base = triangle[i]
        next_base = [1]
        for j in range(len(curr_base)):
            next_base.append(sum(curr_base[j: j + 2]))

        triangle.append(next_base)

    return triangle

get_magic_triangle(7)