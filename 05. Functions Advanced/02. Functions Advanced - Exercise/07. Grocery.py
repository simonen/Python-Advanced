def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    data = []
    for (product, quantity) in result:
        data.append(f"{product}: {quantity}")
    return '\n'.join(data)


print(grocery_store(
 bread=15,
 pasta=12,
 eggs=12,
))
print()
print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))