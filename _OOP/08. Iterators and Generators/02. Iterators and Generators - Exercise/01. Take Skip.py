class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count > 0:
            i = self.start
            self.count -= 1
            self.start += self.step
            return i
        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
 print(number)