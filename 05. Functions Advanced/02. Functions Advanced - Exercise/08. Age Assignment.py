def age_assignment(*args, **kwargs):
    dict = {}
    for name in args:
        if name[0] in kwargs:
            dict[name] = kwargs[name[0]]

    volks = []
    folks = sorted(dict.items(), key=lambda x: x[0])
    for i in folks:
        volks.append(f"{i[0]} is {i[1]} years old.")

    return '\n'.join(volks)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))
