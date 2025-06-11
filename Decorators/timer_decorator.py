from time import sleep, time


def timer(func):
    def wrapper(*args, **kwargs):

        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"{func.__name__} ran for {(end-start):.2f} sec")

        return result

    return wrapper


@timer
def test(n):
    sleep(n)


test(4)