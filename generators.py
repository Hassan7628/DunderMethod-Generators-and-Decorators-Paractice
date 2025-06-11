list1 = [22, 33, 44, 55, 66]


def Gen(lst):
    it = iter(lst)

    while True:
        try:
            yield next(it)

        except StopIteration:
            break


generator = Gen(list1)

for item in generator:
    print(item)


for i in list1:
    print(i)


# Legacy method:
class Legacy:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable) > self.index:
            result = self.iterable[self.index]

            self.index += 1
            return result

        else:
            raise StopIteration


lst = Legacy(list1)

for item in lst:
    print(item)


# New method:
class new:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for item in self.iterable:
            yield item


lst2 = new(list1)

for item in lst2:
    print(item)