from time import sleep


def cache(func):
    cache_value = {}

    def wrapper(*args):

        if args in cache_value:
            return cache_value[args]

        result = func(*args)
        cache_value[args] = result

        return result

    return wrapper


@cache
def add(a, b):
    sleep(2)
    return a + b


print(add(2, 5))
print(add(5, 5))
print(add(2, 5))