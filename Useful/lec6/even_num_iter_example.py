class MyIter:
    def __init__(self, limit):
        self.n = 0
        self.i = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.limit:
            a = self.n
            self.n += 2
            self.i += 1
            return a
        else:
            raise StopIteration


for each in MyIter(13):
    print(each)
# i = iter(x)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


