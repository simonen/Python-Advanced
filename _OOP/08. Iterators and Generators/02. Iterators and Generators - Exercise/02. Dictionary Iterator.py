class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.start = 0
        self.end = len(dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            i = self.start
            self.start += 1
            return list(zip(self.dictionary.keys(), self.dictionary.values()))[i]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
