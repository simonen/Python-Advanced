def words_sorting(*words):
    book = {}
    for word in words:
        if word not in book:
            book[word] = 0
        book[word] += sum(ord(i) for i in word)

    sorted_book = sorted(book.items(), key=lambda x: -x[1] if sum(book.values()) % 2 != 0 else x[0])
    res = [f'{word} - {value}' for word, value in sorted_book]

    return '\n'.join(res)