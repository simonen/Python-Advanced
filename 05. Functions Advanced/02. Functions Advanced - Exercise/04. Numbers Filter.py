def even_odd_filter(**args):
    for k, v in args.items():
        if k == "even":
            args[k] = [int(x) for x in args[k] if int(x) % 2 == 0]
        elif k == "odd":
            args[k] = [int(x) for x in args[k] if int(x) % 2 != 0]
    dict = {k: v for k, v in sorted(args.items(), key=lambda x: -len(x[1]))}

    return dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
