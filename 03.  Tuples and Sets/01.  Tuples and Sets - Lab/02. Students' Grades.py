n = int(input())
book = {}

for _ in range(n):
    students = input().split()
    name, grade = students[0], float(students[1])
    if name not in book:
        book[name] = []

    if int(grade) in range(2, 7):
        book[name].append(grade)

for k, v in book.items():
    avg = sum(v) / len(v)
    print(f"{k} -> {' '.join([f'{i:.2f}' for i in v])} (avg: {avg:.2f})")
