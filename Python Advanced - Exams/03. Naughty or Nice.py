def naughty_or_nice_list(*kids, **kwargs):
    kids_status = {'Nice': [], 'Naughty': [], 'Not found': []}
    found_kids = []

    for i in kids[1:]:
        val = int(i.split("-")[0])
        stat = i.split("-")[1]
        values = [value for value, name in kids[0]]
        for value, name in kids[0]:
            if values.count(value) == 1 and value == val:
                kids_status[stat].append(name)
                found_kids.append((value, name))

    for i in kids[0].copy():
        if i in found_kids:
            kids[0].pop(kids[0].index(i))

    for kid in kwargs:
        names = [kid for value, name in kids[0] if kid == name]
        for value, name in kids[0]:
            if names.count(name) == 1:
                kids_status[kwargs[kid]].append(kid)
                found_kids.append((value, name))

    for i in kids[0].copy():
        if i in found_kids:
            kids[0].pop(kids[0].index(i))

    for i in kids[0]:
        if i not in found_kids:
            kids_status['Not found'].append(i[1])

    res = []
    if kids_status['Nice']:
        res.append(f"Nice: {', '.join(kids_status['Nice'])}")

    if kids_status['Naughty']:
        res.append(f"Naughty: {', '.join(kids_status['Naughty'])}")

    if kids_status['Not found']:
        res.append(f"Not found: {', '.join(kids_status['Not found'])}")

    return "\n".join(res)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (13, "Katy"),
        (11, 'Gion'),
        (3, 'Pena')
    ],
    "3-Nice",
    "13-Naughty",
    '11-Nice',
    '1-Nice',
    '11-Nice',
    '7-Nice',
    Amy="Naughty",
    Katy="Nice",
    Tom='Naughty',
    Gion='Naughty'
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))