def start_spring(**kwargs):
    book = {}
    for k, v in kwargs.items():
        if v not in book:
            book[v] = []
        if k not in book[v]:
            book[v].append(k)

    res = []
    sorted_book = sorted(book.items(), key=lambda x: (-len(x[1]), x[0]))
    for k, v in sorted_book:
        res.append(f'{k}:')
        for i in sorted(v):
            res.append(f'-{i}')

    return '\n'.join(res)