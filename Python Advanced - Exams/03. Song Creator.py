def add_songs(*songs):
    songz = {}
    res = []
    for title, lyrics in songs:
        if f'- {title}' not in songz:
            songz[f'- {title}'] = []
        for line in lyrics:
            if line not in songz[f'- {title}']:
                songz[f'- {title}'].append(line)

    for song, lyrics in songz.items():
        res.append(song)
        for line in lyrics:
            res.append(line)

    return '\n'.join(res)