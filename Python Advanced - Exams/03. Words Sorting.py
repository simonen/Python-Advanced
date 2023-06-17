def words_sorting(*words):
    book = {word: sum(map(ord, word)) for word in words}

    sorted_book = sorted(book.items(), key=lambda x: -x[1] if sum(book.values()) % 2 != 0 else x[0])
    res = [f'{word} - {value}' for word, value in sorted_book]

    return '\n'.join(res)