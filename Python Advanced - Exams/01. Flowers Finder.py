vowels = input().split()
consonants = input().split()

words = {'rose': [], 'daffodil': [], 'tulip': [], 'lotus': []}
is_found = False

while vowels and consonants:
    vowel = vowels.pop(0)
    consonant = consonants.pop()

    for word, letters in words.items():
        if vowel in word:
            words[word].append(vowel)
        if consonant in word:
            words[word].append(consonant)

        if all(x in letters for x in word):
            is_found = True
            print(f"Word found: {word}")
            break

    if is_found:
        break

if not is_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")