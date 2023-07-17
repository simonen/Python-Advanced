from math import ceil


class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.start = 0
        self.ext_seq = ceil(self.number / len(sequence)) * self.sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.number:
            i = self.start
            self.start += 1
            return self.ext_seq[i]
        else:
            raise StopIteration



result = sequence_repeat('abc', 5)
print(result.ext_seq)
# for item in result:
#  print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
 print(item, end='')
