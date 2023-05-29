def students_credits(*courses):
    total_credits = 0
    book = {}
    for i in courses:
        data = i.split("-")
        course = data[0]
        creditz = int(data[1])
        ratio = int(data[3]) / int(data[2])
        d_credits = creditz * ratio
        total_credits += d_credits
        book[course] = d_credits

    sorted_book = sorted(book.items(), key=lambda x: -x[1])
    result = []

    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.")
    for course, score in sorted_book:
        result.append(f"{course} - {score:.1f}")

    return '\n'.join(result)

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)