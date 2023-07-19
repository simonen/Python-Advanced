class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.index = -1
        self.end = len(dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.end - 1:
            raise StopIteration

        self.index += 1

        return list(self.dictionary.items())[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
