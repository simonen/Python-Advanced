def movie_organizer(*movies):
    book = {}
    for title, genre in movies:
        if genre not in book:
            book[genre] = []
        book[genre].append(title)

    catalogue = sorted(book.items(), key=lambda x: (-len(x[1]), x[0]))
    sorted_cat = []

    for group in catalogue:
        genre = group[0]
        movies = group[1]
        sorted_cat.append(f"{genre} - {len(movies)}")
        for movie in sorted(movies):
            sorted_cat.append(f"* {movie}")

    return "\n".join(sorted_cat)


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))