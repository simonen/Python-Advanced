def concatenate(*args, **string):
    args = "".join(list(args))
    for key in string:
        if key in args:
            args = args.replace(key, string[key])
    return args


# print(concatenate("Soft", "UNI", "Is", "Grate", "!",
# UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
