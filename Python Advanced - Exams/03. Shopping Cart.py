def shopping_cart(*args):
    book = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for i in args:
        if i == 'Stop':
            break
        meal, product = i
        if meal == 'Soup' and len(book['Soup']) < 3 and product not in book['Soup']:
            book['Soup'].append(product)
        elif meal == 'Pizza' and len(book['Pizza']) < 4 and product not in book['Pizza']:
            book['Pizza'].append(product)
        elif meal == 'Dessert' and len(book['Dessert']) < 2 and product not in book['Dessert']:
            book['Dessert'].append(product)

    if all(len(v) == 0 for k, v in book.items()):
        return "No products in the cart!"

    for k, v in book.items():
        book[k] = sorted(v)

    cart = sorted(book.items(), key=lambda x: (-len(x[1]), x[0]))
    res = []

    for meal, products in cart:
        res.append(f"{meal}:")
        for product in products:
            res.append(f" - {product}")

    return "\n".join(res)