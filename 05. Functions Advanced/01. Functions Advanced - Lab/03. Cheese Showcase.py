def sorting_cheeses(**kwargs):
    chiiz = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    res = []
    for cheese, quantity in chiiz:
        res.append(cheese)
        quantity_list = sorted(quantity, key=lambda x: -x)
        res += quantity_list
    return '\n'.join(str(x) for x in res)


# cheese = {'Parmesan': [102, 120, 135],
#           'Camembert': [100, 100, 105, 500, 430],
#           'Mozzarella': [50, 125, 90]
#           }
#
# sorting_cheeses(cheese)

print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
