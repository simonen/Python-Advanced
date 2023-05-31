seats = input().split(', ')
seq1 = list(map(int, input().split(', ')))
seq2 = list(map(int, input().split(', ')))

taken = []
rotations = 10

while rotations:
    first = seq1.pop(0)
    last = seq2.pop()
    letter = chr(first + last)
    rotations -= 1
    validate = [str(first) + letter, str(last) + letter]

    for i in range(2):
        if validate[i] in seats and validate[i] not in taken:
            taken.append(validate[i])
            seats.pop(seats.index(validate[i]))
        else:
            seq1.append(first)
            seq2.insert(0, last)

    if len(taken) == 3:
        break

print(f"Seat matches: {', '.join(taken)}")
print(f"Rotations count: {10 - rotations}")