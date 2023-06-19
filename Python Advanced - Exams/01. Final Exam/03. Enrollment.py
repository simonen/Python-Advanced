def gather_credits(credits_needed, *args):
    enrolled = []
    gathered_credits = 0

    for course, credit in args:
        if credits_needed > gathered_credits and course not in enrolled:
            enrolled.append(course)
            gathered_credits += credit

    if credits_needed <= gathered_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(enrolled))}"

    return f"You need to enroll in more courses! You have to gather {credits_needed - gathered_credits} credits more."


print(gather_credits(
    0,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print("------------------")
print(gather_credits(
    90,
    ("Basics", 80),
    ("Bass", 1),
    ("Bai", 2),
    ("Bandamentals", 7),
    # ("Advanced", 10),
    # ("Web", 100)
))
