def solution():
    def integers():
        start = 1
        while True:
            yield start
            start += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
# print(type(halves()))
# print(type(take(5, [])))
print(take(5, halves()))

print(list(map(lambda x: x.__name__, solution())))